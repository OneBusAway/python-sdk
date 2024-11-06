from helpers.load_env import load_settings

from onebusaway import OnebusawaySDK

settings = load_settings(
    {
        "api_key": "TEST",
        "base_url": "https://api.pugetsound.onebusaway.org/",
    }
)

oba = OnebusawaySDK(**settings)

# Search for stops with the word "crystal" in them.
search_input = "crystal"

# Retrieve the search results.
response = oba.search_for_stop.list(input=search_input, max_count=5)

print(response.data)
