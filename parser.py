import json
import time
from datetime import datetime
from typing import Counter

import requests
from fake_useragent import UserAgent
from requests.models import encode_multipart_formdata

all_proxies = []
ua = UserAgent()
user_agent = ua.random
headers = {"User-Agent": user_agent}
counter = 0
total_pages = 72


def parsing_process():
    global counter

    start_time = time.time()
    start_time_str = datetime.fromtimestamp(start_time).strftime("%Y-%m-%d %H:%M:%S")

    print(f"\n[+] Starting parsing proxy-servers at {start_time_str}")
    while counter <= total_pages:
        url = f"https://proxylist.geonode.com/api/proxy-list?limit=100&page={counter}&sort_by=lastChecked&sort_type=desc"

        print(f"[+] Processing page {counter}/{total_pages}...")

        try:
            re = requests.get(url, headers=headers)

            if re.status_code == 429:
                retry_after = re.headers.get("Retry-After")
                if retry_after:
                    print(f"Rate limit hit. Retrying after {retry_after} seconds...")
                    time.sleep(int(retry_after))
                else:
                    print("Rate limit hit. Sleeping for 60 seconds...")
                    time.sleep(60)
                continue

            re.raise_for_status()

            data = re.json()
            if "data" in data and data["data"]:
                all_proxies.extend(data["data"])
                print(
                    f"[+] Page {counter} processed. Found {len(data['data'])} proxies."
                )
            else:
                print(f"No data on page {counter}, stopping.")
                break
        except requests.exceptions.RequestException as ex:
            print(f"Error fetching data from page {counter}: {ex}")
            break

        counter += 1
        time.sleep(1)

    end_time = time.time()
    end_time_str = datetime.fromtimestamp(end_time).strftime("%Y-%m-%d %H:%M:%S")
    duration = end_time - start_time

    print(f"\nProcess completed at {end_time_str}. Duration: {duration:.2f} seconds")

    if all_proxies:
        with open("result.json", "w", encoding="utf-8") as file:
            json.dump(all_proxies, file, indent=4, ensure_ascii=False)
        print(f"Successfully saved {len(all_proxies)} proxies to result.json")
    else:
        print("No proxies found!")
