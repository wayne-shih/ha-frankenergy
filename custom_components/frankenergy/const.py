"""Constants for the Frank Energy Energy sensors."""

from homeassistant.const import Platform

DOMAIN = "frankenergy"
SENSOR_NAME = "Frank Energy"
CONF_START_DATE = "start_date"

PLATFORMS = [
    Platform.SENSOR,
]
