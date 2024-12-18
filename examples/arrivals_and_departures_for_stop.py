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

# Define the query parameters
query = {
    "tripId": "1_604670535",  # Replace with actual trip ID
    "serviceDate": "1810918000000",  # Replace with actual service date in milliseconds since epoch
}

stopId = "1_75403"  # Replace with actual stop ID

# Retrieve arrival and departure information
response = oba.arrival_and_departure.list(stopId, extra_query=query)

# Example to access specific data
arrivals_and_departures = response.data.entry.arrivals_and_departures

for arr_dep in arrivals_and_departures:
    print(f"Route: {arr_dep.route_short_name}")
    print(f"Trip Headsign: {arr_dep.trip_headsign}")
    print(f"Predicted Arrival Time: {arr_dep.predicted_arrival_time}")
    print(f"Scheduled Arrival Time: {arr_dep.scheduled_arrival_time}")
    print(f"Vehicle ID: {arr_dep.vehicle_id}")
    print("")
