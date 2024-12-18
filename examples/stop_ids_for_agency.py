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

stop_ids = oba.stop_ids_for_agency.list(agency_id)
if stop_ids.data and stop_ids.data.list:
    for stop_id in stop_ids.data.list:
        print(stop_id)
