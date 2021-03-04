"""Plugwise Climate component for Home Assistant."""

import logging

from plugwise.exceptions import PlugwiseException

from homeassistant.components.climate import ClimateEntity
from homeassistant.components.climate.const import (
    CURRENT_HVAC_COOL,
    CURRENT_HVAC_HEAT,
    CURRENT_HVAC_IDLE,
    HVAC_MODE_AUTO,
    HVAC_MODE_HEAT,
    HVAC_MODE_HEAT_COOL,
    HVAC_MODE_OFF,
    PRESET_AWAY,
    PRESET_HOME,
    PRESET_NONE,
    SUPPORT_PRESET_MODE,
    SUPPORT_TARGET_TEMPERATURE,
)
from homeassistant.const import ATTR_NAME, ATTR_TEMPERATURE, TEMP_CELSIUS
from homeassistant.core import callback

from .gateway import SmileGateway
from .const import (
    API,
    COORDINATOR,
    DEFAULT_MAX_TEMP,
    DEFAULT_MIN_TEMP,
    DOMAIN,
    PW_CLASS,
    PW_LOCATION,
    PW_MODEL,
    SCHEDULE_OFF,
    SCHEDULE_ON,
    THERMOSTAT_CLASSES,
)

HVAC_MODES_HEAT_ONLY = [HVAC_MODE_HEAT, HVAC_MODE_AUTO, HVAC_MODE_OFF]
HVAC_MODES_HEAT_COOL = [HVAC_MODE_HEAT_COOL, HVAC_MODE_AUTO, HVAC_MODE_OFF]

SUPPORT_FLAGS = SUPPORT_TARGET_TEMPERATURE | SUPPORT_PRESET_MODE

_LOGGER = logging.getLogger(__name__)


async def async_setup_entry(hass, config_entry, async_add_entities):
    """Set up the Smile Thermostats from a config entry."""
    api = hass.data[DOMAIN][config_entry.entry_id][API]
    coordinator = hass.data[DOMAIN][config_entry.entry_id][COORDINATOR]

    entities = []
    devices = api.get_all_devices()

    for dev_id in devices:

        if devices[dev_id][PW_CLASS] not in THERMOSTAT_CLASSES:
            continue

        _LOGGER.debug("Plugwise climate Dev %s", devices[dev_id][ATTR_NAME])
        thermostat = PwThermostat(
            api,
            coordinator,
            devices[dev_id][ATTR_NAME],
            dev_id,
            devices[dev_id][PW_LOCATION],
            devices[dev_id][PW_MODEL],
            DEFAULT_MIN_TEMP,
            DEFAULT_MAX_TEMP,
        )

        entities.append(thermostat)
        _LOGGER.info("Added climate.%s", "{}".format(devices[dev_id][ATTR_NAME]))

    async_add_entities(entities, True)


class PwThermostat(SmileGateway, ClimateEntity):
    """Representation of a Plugwise (zone) thermostat."""

    def __init__(
        self, api, coordinator, name, dev_id, loc_id, model, min_temp, max_temp
    ):
        """Set up the Plugwise API."""
        super().__init__(api, coordinator, name, dev_id)

        self._api = api
        self._loc_id = loc_id
        self._max_temp = max_temp
        self._min_temp = min_temp
        self._model = model

        self._cooling_state = None
        self._compressor_state = None
        self._dhw_state = None
        self._heating_state = None
        self._hvac_mode = None
        self._last_active_schema = None
        self._mode_off = None
        self._preset_mode = None
        self._presets = None
        self._presets_list = None
        self._schedule_temp = None
        self._schema_names = None
        self._schema_status = None
        self._selected_schema = None
        self._setpoint = None
        self._temperature = None
        self._water_pressure = None

        self._single_thermostat = self._api.single_master_thermostat()
        self._unique_id = f"{dev_id}-climate"

    @property
    def hvac_action(self):
        """Return the current action."""
        if self._single_thermostat:
            if self._heating_state:
                return CURRENT_HVAC_HEAT
            if self._cooling_state:
                return CURRENT_HVAC_COOL
            return CURRENT_HVAC_IDLE

        if self._setpoint > self._temperature:
            return CURRENT_HVAC_HEAT

        return CURRENT_HVAC_IDLE

    @property
    def supported_features(self):
        """Return the list of supported features."""
        return SUPPORT_FLAGS

    @property
    def device_state_attributes(self):
        """Return the device specific state attributes."""
        attributes = {}
        if self._schema_names:
            attributes["available_schemas"] = self._schema_names
        if self._selected_schema:
            attributes["selected_schema"] = self._selected_schema
        return attributes

    @property
    def preset_modes(self):
        """Return the available preset modes list."""
        return self._presets_list

    @property
    def hvac_modes(self):
        """Return the available hvac modes list."""
        if self._compressor_state is not None:
            return HVAC_MODES_HEAT_COOL
        return HVAC_MODES_HEAT_ONLY

    @property
    def hvac_mode(self):
        """Return current active hvac state."""
        return self._hvac_mode

    @property
    def target_temperature(self):
        """Return the target_temperature."""
        return self._setpoint

    @property
    def preset_mode(self):
        """Return the active preset."""
        if self._presets:
            return self._preset_mode
        return None

    @property
    def current_temperature(self):
        """Return the current room temperature."""
        return self._temperature

    @property
    def min_temp(self):
        """Return the minimal temperature possible to set."""
        return self._min_temp

    @property
    def max_temp(self):
        """Return the maximum temperature possible to set."""
        return self._max_temp

    @property
    def temperature_unit(self):
        """Return the unit of measured temperature."""
        return TEMP_CELSIUS

    async def async_set_temperature(self, **kwargs):
        """Set new target temperature."""
        temperature = kwargs.get(ATTR_TEMPERATURE)
        if (temperature is not None) and (
            self._min_temp < temperature < self._max_temp
        ):
            _LOGGER.debug("Set temp to %sºC", temperature)
            try:
                await self._api.set_temperature(self._loc_id, temperature)
                self._setpoint = temperature
                self.async_write_ha_state()
            except PlugwiseException:
                _LOGGER.error("Error while communicating to device")
        else:
            _LOGGER.error("Invalid temperature requested")

    async def async_set_hvac_mode(self, hvac_mode):
        """Set the hvac mode."""
        _LOGGER.debug("Set hvac_mode to: %s", hvac_mode)
        state = SCHEDULE_OFF
        if hvac_mode == HVAC_MODE_AUTO:
            state = SCHEDULE_ON
            try:
                await self._api.set_temperature(self._loc_id, self._schedule_temp)
                self._setpoint = self._schedule_temp
            except PlugwiseException:
                _LOGGER.error("Error while communicating to device")
        try:
            await self._api.set_schedule_state(
                self._loc_id, self._last_active_schema, state
            )
            self._mode_off = False
            if hvac_mode == HVAC_MODE_OFF:
                self._mode_off = True
                preset_mode = PRESET_AWAY
                await self._api.set_preset(self._loc_id, preset_mode)
                self._preset_mode = preset_mode
                self._setpoint = self._presets.get(self._preset_mode, PRESET_NONE)[0]
            if hvac_mode == HVAC_MODE_HEAT and self._preset_mode == PRESET_AWAY:
                preset_mode = PRESET_HOME
                await self._api.set_preset(self._loc_id, preset_mode)
                self._preset_mode = preset_mode
                self._setpoint = self._presets.get(self._preset_mode, PRESET_NONE)[0]
            self._hvac_mode = hvac_mode
            self.async_write_ha_state()
        except PlugwiseException:
            _LOGGER.error("Error while communicating to device")

    async def async_set_preset_mode(self, preset_mode):
        """Set the preset mode."""
        _LOGGER.debug("Set preset mode to %s.", preset_mode)
        try:
            await self._api.set_preset(self._loc_id, preset_mode)
            self._preset_mode = preset_mode
            self._setpoint = self._presets.get(self._preset_mode, PRESET_NONE)[0]
            self.async_write_ha_state()
        except PlugwiseException:
            _LOGGER.error("Error while communicating to device")

    @callback
    def _async_process_data(self):
        """Update the data for this climate device."""
        _LOGGER.info("Updating climate...")
        climate_data = self._api.get_device_data(self._dev_id)
        heater_central_data = self._api.get_device_data(self._api.heater_id)

        self._setpoint = climate_data.get("setpoint")
        self._temperature = climate_data.get("temperature")
        self._schedule_temp = climate_data.get("schedule_temperature")
        self._schema_names = climate_data.get("available_schedules")
        if "selected_schedule" in climate_data:
            self._selected_schema = climate_data["selected_schedule"]
            self._schema_status = False
            if self._selected_schema is not None:
                self._schema_status = True
        self._last_active_schema = climate_data.get("last_used")
        self._presets = climate_data.get("presets")
        if self._presets:
            self._presets_list = list(self._presets)
        self._preset_mode = climate_data.get("active_preset")

        self._heating_state = heater_central_data.get("heating_state")
        self._cooling_state = heater_central_data.get("cooling_state")
        self._compressor_state = heater_central_data.get("compressor_state")

        self._hvac_mode = HVAC_MODE_HEAT
        if self._compressor_state is not None:
            self._hvac_mode = HVAC_MODE_HEAT_COOL
        if self._schema_status:
            self._hvac_mode = HVAC_MODE_AUTO
        if self._mode_off:
            self._hvac_mode = HVAC_MODE_OFF

        self.async_write_ha_state()
