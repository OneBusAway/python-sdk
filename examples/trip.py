import onebusaway


def main_sync() -> None:
    client = onebusaway.OnebusawaySDK(api_key="TEST")

    trip_id = "40_608344966"
    trip = client.trip.retrieve(trip_id)

    if trip.data and trip.data.entry:
        print(trip.data.entry)
    else:
        print("trip data or entry is None.")


if __name__ == "__main__":
    main_sync()
