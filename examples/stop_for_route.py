from pprint import pprint

from helpers.load_env import load_settings

from onebusaway import OnebusawaySDK

# Load settings from .env file, if it exists. If not, we'll use the
# Puget Sound server URL (which is also the default in the SDK) and
# the 'TEST' API key.
settings = load_settings(
    {
        "api_key": "TEST",
        "base_url": "https://api.pugetsound.onebusaway.org/",
    }
)

# Create a new instance of the OneBusAway SDK with the settings we loaded.
oba = OnebusawaySDK(**settings)

route_id = "1_100224"
response = oba.stops_for_route.list(route_id)

if response and response.data:
    pprint(response.data)
