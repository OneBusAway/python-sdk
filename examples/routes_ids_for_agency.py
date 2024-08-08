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

agency_id = "40"  # Link Light Rail in the Seattle area.

route_ids = oba.route_ids_for_agency.list(agency_id)
if route_ids.data and route_ids.data.list:
    for route_id in route_ids.data.list:
        print(route_id)
