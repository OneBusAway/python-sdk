import onebusaway


def main_sync() -> None:
    client = onebusaway.OnebusawaySDK(api_key="TEST")
    stop_id = "1_75403"
    schedule_for_stop = client.schedule_for_stop.retrieve(stop_id)

    if schedule_for_stop.data and schedule_for_stop.data.entry:
        print(schedule_for_stop.data.entry)
    else:
        print("schedule data or entry is None.")


if __name__ == "__main__":
    main_sync()
