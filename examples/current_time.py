from onebusaway import OnebusawaySDK
from helpers.load_env import load_settings
from pprint import pprint


# Load settings from .env file, if it exists. If not, we'll use the
# Puget Sound server URL (which is also the default in the SDK) and
# the 'TEST' API key.
settings = load_settings({
    "api_key": "TEST",
    "base_url": "https://api.pugetsound.onebusaway.org/",
})

# Create a new instance of the OneBusAway SDK with the settings we loaded.
oba = OnebusawaySDK(**settings)

response = oba.current_time.retrieve()
pprint(response)
