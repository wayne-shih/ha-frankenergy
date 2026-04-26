"""Config flow for Frank Energy integration."""

from homeassistant import config_entries
from homeassistant.const import CONF_EMAIL, CONF_PASSWORD
import homeassistant.helpers.config_validation as cv
import voluptuous as vol

from .const import DOMAIN, SENSOR_NAME, CONF_START_DATE


@config_entries.HANDLERS.register(DOMAIN)
class FrankEnergyConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    """Define the config flow."""

    VERSION = 1

    async def async_step_user(self, user_input=None):
        """Show user form."""
        if user_input is not None:
            return self.async_create_entry(
                title=SENSOR_NAME,
                data={
                    CONF_EMAIL: user_input[CONF_EMAIL],
                    CONF_PASSWORD: user_input[CONF_PASSWORD],
                    CONF_START_DATE: user_input.get(CONF_START_DATE, ""),
                },
            )

        return self.async_show_form(
            step_id="user",
            data_schema=vol.Schema(
                {
                    vol.Required(CONF_EMAIL, description="Enter your email"): cv.string,
                    vol.Required(
                        CONF_PASSWORD, description="Enter your password"
                    ): cv.string,
                    vol.Optional(
                        CONF_START_DATE,
                        description="Account start date (YYYY-MM-DD) for historical import, leave blank for last 4 days",
                    ): cv.string,
                }
            ),
        )
