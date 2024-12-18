import onebusaway


def main_sync() -> None:
    client = onebusaway.OnebusawaySDK(api_key="TEST")

    agency_id = "40"
    agency = client.vehicles_for_agency.list(agency_id)

    if agency.data and agency.data.list:
        print(agency.data.list)
    else:
        print("Agency data or list is None.")


if __name__ == "__main__":
    main_sync()
