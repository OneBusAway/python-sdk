

import onebusaway


def main_sync() -> None:
    client = onebusaway.OnebusawaySDK(api_key="TEST")
    agency = client.agency.retrieve("1")

    if agency.data and agency.data.entry:
        print(agency.data.entry)
    else:
        print("Agency data or entry is None.")

if __name__ == "__main__":
    main_sync()
