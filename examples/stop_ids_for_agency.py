

import onebusaway


def main_sync() -> None:
    client = onebusaway.OnebusawaySDK(api_key="TEST")
    agency_id = "40";
    stop_ids = client.stop_ids_for_agency.list(agency_id)
    if stop_ids.data:
        for stop_id in stop_ids.data.list:
            print(stop_id)


if __name__ == "__main__":
    main_sync()
