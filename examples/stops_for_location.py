from typing import Any

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

space_needle_stops = oba.stops_for_location.list(
    lat=47.6205,
    lon=-122.3493,
)

stops = space_needle_stops.data.list
references = space_needle_stops.data.references

# make it easy to look up routes by ID.
reference_map = {}
for ref_route in references.routes:
    reference_map[ref_route.id] = ref_route

for stop in stops:
    print(f"{stop.name} ({stop.lat}, {stop.lon})")
    print("  Routes:")

    for route_id in stop.route_ids:
        # TODO: add type to route
        route: Any = reference_map[route_id] # type: ignore

        # Get a string that looks like "D Line - Blue Ridge/Crown Hill - Ballard - Downtown Seattle"
        description_list = [route.null_safe_short_name, route.description] # type: ignore
        description_list = [e for e in description_list if e] # type: ignore
        description_str = " - ".join(description_list) # type: ignore
        print(f"    {description_str}")
