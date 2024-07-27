

import onebusaway


def main_sync() -> None:
    client = onebusaway.OnebusawaySDK(api_key="TEST")
    stop = client.stop.retrieve("1_75403")

    if stop.data and stop.data.entry:
        print(stop.data.entry)
    else:
        print("stop not found")

if __name__ == "__main__":
    main_sync()
