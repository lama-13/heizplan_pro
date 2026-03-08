import logging
from homeassistant.core import HomeAssistant
from homeassistant.helpers.typing import ConfigType

_LOGGER = logging.getLogger(__name__)
DOMAIN = "heizplan_pro"

async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool:
    """Setzt die Heizplan Pro Integration auf."""
    # Registriert den statischen Pfad, damit das HTML erreichbar ist
    # Erreichbar unter: http://HA-IP:8123/heizplan_pro/index.html
    hass.http.register_static_path(
        "/heizplan_pro",
        hass.config.path("custom_components/heizplan_pro/www"),
        True
    )
    _LOGGER.info("Heizplan Pro www-Pfad registriert")
    return True
