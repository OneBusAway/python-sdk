import onebusaway


def main_sync():
    client = onebusaway.OnebusawaySDK(api_key="TEST")
    agency = client.agency.retrieve("1")

    if agency.data and agency.data.entry:
        print(agency.data.entry)
    else:
        print("Agency data or entry is None.")


if __name__ == "__main__":
    print("Running synchronous main function:")
    main_sync()

# import asyncio
# import sys

# async def main_async():
#     client = onebusaway.AsyncOnebusawaySDK(api_key="TEST")
#     agency = await client.agency.retrieve('1')

#     if agency.data and agency.data.entry:
#         print(agency.data.entry)
#     else:
#         print("Agency data or entry is None.")

# if __name__ == "__main__":
#     if sys.platform.startswith('win'):
#         asyncio.set_event_loop_policy(asyncio.WindowsProactorEventLoopPolicy())
#     print("Running asynchronous main function:")
#     asyncio.run(main_async())
