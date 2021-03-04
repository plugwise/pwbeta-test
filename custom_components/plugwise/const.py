"""Constants for Plugwise beta component."""

from homeassistant.components.binary_sensor import DEVICE_CLASS_MOTION
from homeassistant.components.switch import DEVICE_CLASS_OUTLET
from homeassistant.const import (
    ATTR_DEVICE_CLASS,
    ATTR_ICON,
    ATTR_NAME,
    ATTR_STATE,
    ATTR_UNIT_OF_MEASUREMENT,
    DEVICE_CLASS_BATTERY,
    DEVICE_CLASS_ILLUMINANCE,
    DEVICE_CLASS_POWER,
    DEVICE_CLASS_PRESSURE,
    DEVICE_CLASS_SIGNAL_STRENGTH,
    DEVICE_CLASS_TEMPERATURE,
    ENERGY_KILO_WATT_HOUR,
    ENERGY_WATT_HOUR,
    PERCENTAGE,
    POWER_WATT,
    PRESSURE_BAR,
    SIGNAL_STRENGTH_DECIBELS_MILLIWATT,
    TEMP_CELSIUS,
    TIME_MILLISECONDS,
    VOLUME_CUBIC_METERS,
)

API = "api"
ATTR_ENABLED_DEFAULT = "enabled_default"
DOMAIN = "plugwise"
COORDINATOR = "coordinator"
GATEWAY = "gateway"
PW_CLASS = "class"
PW_LOCATION = "location"
PW_MODEL = "model"
PW_TYPE = "plugwise_type"
SCHEDULE_OFF = "false"
SCHEDULE_ON = "true"
SMILE = "smile"
STICK = "stick"
STRETCH = "stretch"
STRETCH_USERNAME = "stretch"
DEVICE_STATE = "device_state"
UNIT_LUMEN = "lm"
USB = "usb"

FLOW_NET = "flow_network"
FLOW_TYPE = "flow_type"
FLOW_USB = "flow_usb"
FLOW_SMILE = "smile (Adam/Anna/P1)"
FLOW_STRETCH = "stretch (Stretch)"

UNDO_UPDATE_LISTENER = "undo_update_listener"

# Default directives
DEFAULT_MAX_TEMP = 30
DEFAULT_MIN_TEMP = 4
DEFAULT_NAME = "Smile"
DEFAULT_PORT = 80
DEFAULT_SCAN_INTERVAL = {
    "power": 10,
    "stretch": 60,
    "thermostat": 60,
}
DEFAULT_TIMEOUT = 10
DEFAULT_USERNAME = "smile"

# Configuration directives
CONF_MAX_TEMP = "max_temp"
CONF_MIN_TEMP = "min_temp"

# Icons
COOL_ICON = "mdi:snowflake"
FLAME_ICON = "mdi:fire"
FLOW_OFF_ICON = "mdi:water-pump-off"
FLOW_ON_ICON = "mdi:water-pump"
HEATING_ICON = "mdi:radiator"
IDLE_ICON = "mdi:circle-off-outline"
NOTIFICATION_ICON = "mdi:mailbox-up-outline"
NO_NOTIFICATION_ICON = "mdi:mailbox-outline"
SWITCH_ICON = "mdi:electric-switch"

# --- Const for Plugwise Smile and Stretch

PLATFORMS_GATEWAY = ["binary_sensor", "climate", "sensor", "switch"]
SENSOR_PLATFORMS = ["sensor", "switch"]
SERVICE_DELETE = "delete_notification"

# Climate const:
THERMOSTAT_CLASSES = [
    "thermostat",
    "zone_thermostat",
    "thermostatic_radiator_valve",
]

# Config_flow const:
ZEROCONF_MAP = {
    "smile": "P1",
    "smile_thermo": "Anna",
    "smile_open_therm": "Adam",
    "stretch": "Stretch",
}

# Binary sensor map:
GW_BINARY_SENSORS = {
    "dhw_state": {
        ATTR_DEVICE_CLASS: None,
        ATTR_ENABLED_DEFAULT: True,
        ATTR_ICON: None,
        ATTR_NAME: "Auxiliary Dhw State",
        ATTR_UNIT_OF_MEASUREMENT: None,
    },
    "flame_state": {
        ATTR_DEVICE_CLASS: None,
        ATTR_ENABLED_DEFAULT: True,
        ATTR_ICON: None,
        ATTR_NAME: "Auxiliary Flame State",
        ATTR_UNIT_OF_MEASUREMENT: None,
    },
    "slave_boiler_state": {
        ATTR_DEVICE_CLASS: None,
        ATTR_ENABLED_DEFAULT: True,
        ATTR_ICON: None,
        ATTR_NAME: "Auxiliary Secondary Heater Device State",
        ATTR_UNIT_OF_MEASUREMENT: None,
    },
}

# Sensor maps:
THERMOSTAT_SENSORS = {
    "battery": {
        ATTR_DEVICE_CLASS: DEVICE_CLASS_BATTERY,
        ATTR_ENABLED_DEFAULT: True,
        ATTR_ICON: None,
        ATTR_NAME: "Battery",
        ATTR_UNIT_OF_MEASUREMENT: PERCENTAGE,
    },
    "illuminance": {
        ATTR_DEVICE_CLASS: DEVICE_CLASS_ILLUMINANCE,
        ATTR_ENABLED_DEFAULT: True,
        ATTR_ICON: None,
        ATTR_NAME: "Illuminance",
        ATTR_UNIT_OF_MEASUREMENT: UNIT_LUMEN,
    },
    "outdoor_temperature": {
        ATTR_DEVICE_CLASS: DEVICE_CLASS_TEMPERATURE,
        ATTR_ENABLED_DEFAULT: True,
        ATTR_ICON: None,
        ATTR_NAME: "Outdoor Temperature",
        ATTR_UNIT_OF_MEASUREMENT: TEMP_CELSIUS,
    },
    "setpoint": {
        ATTR_DEVICE_CLASS: DEVICE_CLASS_TEMPERATURE,
        ATTR_ENABLED_DEFAULT: True,
        ATTR_ICON: None,
        ATTR_NAME: "Setpoint",
        ATTR_UNIT_OF_MEASUREMENT: TEMP_CELSIUS,
    },
    "temperature": {
        ATTR_DEVICE_CLASS: DEVICE_CLASS_TEMPERATURE,
        ATTR_ENABLED_DEFAULT: True,
        ATTR_ICON: None,
        ATTR_NAME: "Temperature",
        ATTR_UNIT_OF_MEASUREMENT: TEMP_CELSIUS,
    },
    "temperature_difference": {
        ATTR_DEVICE_CLASS: DEVICE_CLASS_TEMPERATURE,
        ATTR_ENABLED_DEFAULT: False,
        ATTR_ICON: None,
        ATTR_NAME: "Temperature Difference",
        ATTR_UNIT_OF_MEASUREMENT: TEMP_CELSIUS,
    },
    "valve_position": {
        ATTR_DEVICE_CLASS: None,
        ATTR_ENABLED_DEFAULT: True,
        ATTR_ICON: "mdi:valve",
        ATTR_NAME: "Valve Position",
        ATTR_UNIT_OF_MEASUREMENT: PERCENTAGE,
    },
}

AUX_DEV_SENSORS = {
    "intended_boiler_temperature": {
        ATTR_DEVICE_CLASS: DEVICE_CLASS_TEMPERATURE,
        ATTR_ENABLED_DEFAULT: True,
        ATTR_ICON: None,
        ATTR_NAME: "Auxiliary Intended Boiler Temperature",
        ATTR_UNIT_OF_MEASUREMENT: TEMP_CELSIUS,
    },
    "modulation_level": {
        ATTR_DEVICE_CLASS: None,
        ATTR_ENABLED_DEFAULT: False,
        ATTR_ICON: "mdi:percent",
        ATTR_NAME: "Auxiliary Heater Modulation Level",
        ATTR_UNIT_OF_MEASUREMENT: PERCENTAGE,
    },
    "return_temperature": {
        ATTR_DEVICE_CLASS: DEVICE_CLASS_TEMPERATURE,
        ATTR_ENABLED_DEFAULT: False,
        ATTR_ICON: None,
        ATTR_NAME: "Auxiliary Return Temperature",
        ATTR_UNIT_OF_MEASUREMENT: TEMP_CELSIUS,
    },
    "water_pressure": {
        ATTR_DEVICE_CLASS: DEVICE_CLASS_PRESSURE,
        ATTR_ENABLED_DEFAULT: True,
        ATTR_ICON: None,
        ATTR_NAME: "Auxiliary Water Pressure",
        ATTR_UNIT_OF_MEASUREMENT: PRESSURE_BAR,
    },
    "water_temperature": {
        ATTR_DEVICE_CLASS: DEVICE_CLASS_TEMPERATURE,
        ATTR_ENABLED_DEFAULT: True,
        ATTR_ICON: None,
        ATTR_NAME: "Auxiliary Water Temperature",
        ATTR_UNIT_OF_MEASUREMENT: TEMP_CELSIUS,
    },
}

ENERGY_SENSORS = {
    "electricity_consumed": {
        ATTR_DEVICE_CLASS: DEVICE_CLASS_POWER,
        ATTR_ENABLED_DEFAULT: True,
        ATTR_ICON: None,
        ATTR_NAME: "Electricity Consumed",
        ATTR_UNIT_OF_MEASUREMENT: POWER_WATT,
    },
    "electricity_produced": {
        ATTR_DEVICE_CLASS: DEVICE_CLASS_POWER,
        ATTR_ENABLED_DEFAULT: True,
        ATTR_ICON: None,
        ATTR_NAME: "Electricity Produced",
        ATTR_UNIT_OF_MEASUREMENT: POWER_WATT,
    },
    "electricity_consumed_interval": {
        ATTR_DEVICE_CLASS: DEVICE_CLASS_POWER,
        ATTR_ENABLED_DEFAULT: True,
        ATTR_ICON: None,
        ATTR_NAME: "Electricity Consumed Interval",
        ATTR_UNIT_OF_MEASUREMENT: ENERGY_WATT_HOUR,
    },
    "electricity_consumed_peak_interval": {
        ATTR_DEVICE_CLASS: DEVICE_CLASS_POWER,
        ATTR_ENABLED_DEFAULT: True,
        ATTR_ICON: None,
        ATTR_NAME: "Electricity Consumed Peak Interval",
        ATTR_UNIT_OF_MEASUREMENT: ENERGY_WATT_HOUR,
    },
    "electricity_consumed_off_peak_interval": {
        ATTR_DEVICE_CLASS: DEVICE_CLASS_POWER,
        ATTR_ENABLED_DEFAULT: True,
        ATTR_ICON: None,
        ATTR_NAME: "Electricity Consumed Off Peak Interval",
        ATTR_UNIT_OF_MEASUREMENT: ENERGY_WATT_HOUR,
    },
    "electricity_produced_interval": {
        ATTR_DEVICE_CLASS: DEVICE_CLASS_POWER,
        ATTR_ENABLED_DEFAULT: True,
        ATTR_ICON: None,
        ATTR_NAME: "Electricity Produced Interval",
        ATTR_UNIT_OF_MEASUREMENT: ENERGY_WATT_HOUR,
    },
    "electricity_produced_peak_interval": {
        ATTR_DEVICE_CLASS: DEVICE_CLASS_POWER,
        ATTR_ENABLED_DEFAULT: True,
        ATTR_ICON: None,
        ATTR_NAME: "Electricity Produced Peak Interval",
        ATTR_UNIT_OF_MEASUREMENT: ENERGY_WATT_HOUR,
    },
    "electricity_produced_off_peak_interval": {
        ATTR_DEVICE_CLASS: DEVICE_CLASS_POWER,
        ATTR_ENABLED_DEFAULT: True,
        ATTR_ICON: None,
        ATTR_NAME: "Electricity Produced Off Peak Interval",
        ATTR_UNIT_OF_MEASUREMENT: ENERGY_WATT_HOUR,
    },
    "electricity_consumed_off_peak_point": {
        ATTR_DEVICE_CLASS: DEVICE_CLASS_POWER,
        ATTR_ENABLED_DEFAULT: True,
        ATTR_ICON: None,
        ATTR_NAME: "Electricity Consumed Off Peak Point",
        ATTR_UNIT_OF_MEASUREMENT: POWER_WATT,
    },
    "electricity_consumed_peak_point": {
        ATTR_DEVICE_CLASS: DEVICE_CLASS_POWER,
        ATTR_ENABLED_DEFAULT: True,
        ATTR_ICON: None,
        ATTR_NAME: "Electricity Consumed Peak Point",
        ATTR_UNIT_OF_MEASUREMENT: POWER_WATT,
    },
    "electricity_consumed_off_peak_cumulative": {
        ATTR_DEVICE_CLASS: DEVICE_CLASS_POWER,
        ATTR_ENABLED_DEFAULT: True,
        ATTR_ICON: None,
        ATTR_NAME: "Electricity Consumed Off Peak Cumulative",
        ATTR_UNIT_OF_MEASUREMENT: ENERGY_KILO_WATT_HOUR,
    },
    "electricity_consumed_peak_cumulative": {
        ATTR_DEVICE_CLASS: DEVICE_CLASS_POWER,
        ATTR_ENABLED_DEFAULT: True,
        ATTR_ICON: None,
        ATTR_NAME: "Electricity Consumed Peak Cumulative",
        ATTR_UNIT_OF_MEASUREMENT: ENERGY_KILO_WATT_HOUR,
    },
    "electricity_produced_off_peak_point": {
        ATTR_DEVICE_CLASS: DEVICE_CLASS_POWER,
        ATTR_ENABLED_DEFAULT: True,
        ATTR_ICON: None,
        ATTR_NAME: "Electricity Produced Off Peak Point)",
        ATTR_UNIT_OF_MEASUREMENT: POWER_WATT,
    },
    "electricity_produced_peak_point": {
        ATTR_DEVICE_CLASS: DEVICE_CLASS_POWER,
        ATTR_ENABLED_DEFAULT: True,
        ATTR_ICON: None,
        ATTR_NAME: "Electricity Produced Peak Point",
        ATTR_UNIT_OF_MEASUREMENT: POWER_WATT,
    },
    "electricity_produced_off_peak_cumulative": {
        ATTR_DEVICE_CLASS: DEVICE_CLASS_POWER,
        ATTR_ENABLED_DEFAULT: True,
        ATTR_ICON: None,
        ATTR_NAME: "Electricity Produced Off Peak Cumulative",
        ATTR_UNIT_OF_MEASUREMENT: ENERGY_KILO_WATT_HOUR,
    },
    "electricity_produced_peak_cumulative": {
        ATTR_DEVICE_CLASS: DEVICE_CLASS_POWER,
        ATTR_ENABLED_DEFAULT: True,
        ATTR_ICON: None,
        ATTR_NAME: "Electricity Produced Peak Cumulative",
        ATTR_UNIT_OF_MEASUREMENT: ENERGY_KILO_WATT_HOUR,
    },
    "net_electricity_point": {
        ATTR_DEVICE_CLASS: DEVICE_CLASS_POWER,
        ATTR_ENABLED_DEFAULT: True,
        ATTR_ICON: None,
        ATTR_NAME: "Net Electricity Point",
        ATTR_UNIT_OF_MEASUREMENT: POWER_WATT,
    },
    "net_electricity_cumulative": {
        ATTR_DEVICE_CLASS: DEVICE_CLASS_POWER,
        ATTR_ENABLED_DEFAULT: True,
        ATTR_ICON: None,
        ATTR_NAME: "Net Electricity Cumulative",
        ATTR_UNIT_OF_MEASUREMENT: ENERGY_KILO_WATT_HOUR,
    },
    "gas_consumed_interval": {
        ATTR_DEVICE_CLASS: None,
        ATTR_ENABLED_DEFAULT: True,
        ATTR_ICON: FLAME_ICON,
        ATTR_NAME: "Gas Consumed Interval",
        ATTR_UNIT_OF_MEASUREMENT: VOLUME_CUBIC_METERS,
    },
    "gas_consumed_cumulative": {
        ATTR_DEVICE_CLASS: None,
        ATTR_ENABLED_DEFAULT: True,
        ATTR_ICON: FLAME_ICON,
        ATTR_NAME: "Gas_Consumed_Cumulative",
        ATTR_UNIT_OF_MEASUREMENT: VOLUME_CUBIC_METERS,
    },
}

# Switch const:
SWITCH_CLASSES = ["plug", "switch_group"]

# --- Const for Plugwise USB-stick.

PLATFORMS_USB = ["binary_sensor", "sensor", "switch"]
CONF_USB_PATH = "usb_path"

# Callback types
CB_NEW_NODE = "NEW_NODE"

# Sensor IDs
AVAILABLE_SENSOR_ID = "available"
CURRENT_POWER_SENSOR_ID = "power_1s"
TODAY_ENERGY_SENSOR_ID = "power_con_today"
MOTION_SENSOR_ID = "motion"

# Sensor types
USB_SENSORS = {
    AVAILABLE_SENSOR_ID: {
        ATTR_DEVICE_CLASS: None,
        ATTR_ENABLED_DEFAULT: False,
        ATTR_ICON: "mdi:signal-off",
        ATTR_NAME: "Available",
        ATTR_STATE: "get_available",
        ATTR_UNIT_OF_MEASUREMENT: None,
    },
    "ping": {
        ATTR_DEVICE_CLASS: None,
        ATTR_ENABLED_DEFAULT: False,
        ATTR_ICON: "mdi:speedometer",
        ATTR_NAME: "Ping roundtrip",
        ATTR_STATE: "get_ping",
        ATTR_UNIT_OF_MEASUREMENT: TIME_MILLISECONDS,
    },
    CURRENT_POWER_SENSOR_ID: {
        ATTR_DEVICE_CLASS: DEVICE_CLASS_POWER,
        ATTR_ENABLED_DEFAULT: True,
        ATTR_ICON: None,
        ATTR_NAME: "Power usage",
        ATTR_STATE: "get_power_usage",
        ATTR_UNIT_OF_MEASUREMENT: POWER_WATT,
    },
    "power_8s": {
        ATTR_DEVICE_CLASS: DEVICE_CLASS_POWER,
        ATTR_ENABLED_DEFAULT: False,
        ATTR_ICON: None,
        ATTR_NAME: "Power usage 8 seconds",
        ATTR_STATE: "get_power_usage_8_sec",
        ATTR_UNIT_OF_MEASUREMENT: POWER_WATT,
    },
    "power_con_cur_hour": {
        ATTR_DEVICE_CLASS: DEVICE_CLASS_POWER,
        ATTR_ENABLED_DEFAULT: True,
        ATTR_ICON: None,
        ATTR_NAME: "Power consumption current hour",
        ATTR_STATE: "get_power_consumption_current_hour",
        ATTR_UNIT_OF_MEASUREMENT: ENERGY_KILO_WATT_HOUR,
    },
    "power_con_prev_hour": {
        ATTR_DEVICE_CLASS: DEVICE_CLASS_POWER,
        ATTR_ENABLED_DEFAULT: True,
        ATTR_ICON: None,
        ATTR_NAME: "Power consumption previous hour",
        ATTR_STATE: "get_power_consumption_prev_hour",
        ATTR_UNIT_OF_MEASUREMENT: ENERGY_KILO_WATT_HOUR,
    },
    TODAY_ENERGY_SENSOR_ID: {
        ATTR_DEVICE_CLASS: DEVICE_CLASS_POWER,
        ATTR_ENABLED_DEFAULT: True,
        ATTR_ICON: None,
        ATTR_NAME: "Power consumption today",
        ATTR_STATE: "get_power_consumption_today",
        ATTR_UNIT_OF_MEASUREMENT: ENERGY_KILO_WATT_HOUR,
    },
    "power_con_yesterday": {
        ATTR_DEVICE_CLASS: DEVICE_CLASS_POWER,
        ATTR_ENABLED_DEFAULT: True,
        ATTR_ICON: None,
        ATTR_NAME: "Power consumption yesterday",
        ATTR_STATE: "get_power_consumption_yesterday",
        ATTR_UNIT_OF_MEASUREMENT: ENERGY_KILO_WATT_HOUR,
    },
    "power_prod_cur_hour": {
        ATTR_DEVICE_CLASS: DEVICE_CLASS_POWER,
        ATTR_ENABLED_DEFAULT: False,
        ATTR_ICON: None,
        ATTR_NAME: "Power production current hour",
        ATTR_STATE: "get_power_production_current_hour",
        ATTR_UNIT_OF_MEASUREMENT: ENERGY_KILO_WATT_HOUR,
    },
    "power_prod_prev_hour": {
        ATTR_DEVICE_CLASS: DEVICE_CLASS_POWER,
        ATTR_ENABLED_DEFAULT: False,
        ATTR_ICON: None,
        ATTR_NAME: "Power production previous hour",
        ATTR_STATE: "get_power_production_previous_hour",
        ATTR_UNIT_OF_MEASUREMENT: ENERGY_KILO_WATT_HOUR,
    },
    "RSSI_in": {
        ATTR_DEVICE_CLASS: DEVICE_CLASS_SIGNAL_STRENGTH,
        ATTR_ENABLED_DEFAULT: False,
        ATTR_ICON: None,
        ATTR_NAME: "Inbound RSSI",
        ATTR_STATE: "get_in_RSSI",
        ATTR_UNIT_OF_MEASUREMENT: SIGNAL_STRENGTH_DECIBELS_MILLIWATT,
    },
    "RSSI_out": {
        ATTR_DEVICE_CLASS: DEVICE_CLASS_SIGNAL_STRENGTH,
        ATTR_ENABLED_DEFAULT: False,
        ATTR_ICON: None,
        ATTR_NAME: "Outbound RSSI",
        ATTR_STATE: "get_out_RSSI",
        ATTR_UNIT_OF_MEASUREMENT: SIGNAL_STRENGTH_DECIBELS_MILLIWATT,
    },
}
USB_BINARY_SENSORS = {
    MOTION_SENSOR_ID: {
        ATTR_DEVICE_CLASS: DEVICE_CLASS_MOTION,
        ATTR_ENABLED_DEFAULT: True,
        ATTR_ICON: None,
        ATTR_NAME: "Motion",
        ATTR_STATE: "get_motion",
        ATTR_UNIT_OF_MEASUREMENT: None,
    }
}

# Switch types
SWITCHES = {
    "relay": {
        ATTR_DEVICE_CLASS: DEVICE_CLASS_OUTLET,
        ATTR_ENABLED_DEFAULT: True,
        ATTR_ICON: None,
        ATTR_NAME: "Relay state",
        ATTR_STATE: "get_relay_state",
        "switch": "set_relay_state",
        ATTR_UNIT_OF_MEASUREMENT: "state",
    }
}

ATTR_MAC_ADDRESS = "mac"

ATTR_SCAN_DAYLIGHT_MODE = "day_light"
ATTR_SCAN_SENSITIVITY_MODE = "sensitivity_mode"
ATTR_SCAN_RESET_TIMER = "reset_timer"

ATTR_SED_STAY_ACTIVE = "stay_active"
ATTR_SED_SLEEP_FOR = "sleep_for"
ATTR_SED_MAINTENANCE_INTERVAL = "maintenance_interval"
ATTR_SED_CLOCK_SYNC = "clock_sync"
ATTR_SED_CLOCK_INTERVAL = "clock_interval"

SCAN_SENSITIVITY_HIGH = "high"
SCAN_SENSITIVITY_MEDIUM = "medium"
SCAN_SENSITIVITY_OFF = "off"
SCAN_SENSITIVITY_MODES = [
    SCAN_SENSITIVITY_HIGH,
    SCAN_SENSITIVITY_MEDIUM,
    SCAN_SENSITIVITY_OFF,
]

SERVICE_CONFIGURE_BATTERY = "configure_battery_savings"
SERVICE_CONFIGURE_SCAN = "configure_scan"
SERVICE_DEVICE_ADD = "device_add"
SERVICE_DEVICE_REMOVE = "device_remove"
