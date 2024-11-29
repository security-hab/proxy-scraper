import json
from parser import parsing_process


def proxySelector(
    proxies,
    anonymity_level="elite",
    min_uptime=99.0,
    max_latency=100.0,
    protocol="socks5",
):
    best_proxies = []

    for proxy in proxies:
        if proxy["anonymityLevel"] == anonymity_level:
            if proxy["upTime"] >= min_uptime:
                if proxy["latency"] <= max_latency:
                    if protocol in proxy["protocols"]:
                        best_proxies.append(proxy)
    return best_proxies


def main():
    parsing_process()

    try:
        with open("result.json", "r", encoding="utf-8") as file:
            json_data = file.read()

        proxies = json.loads(json_data)
    except FileNotFoundError:
        print("File result.json not found! Please run the parser first.")
        return
    except json.JSONDecodeError:
        print("Error decoding JSON data from result.json")
        return

    best_proxies = proxySelector(proxies)
    counter = 1
    print("\nBest proxies: ")

    for proxy in best_proxies:
        print(
            f"[{counter}] IP: {proxy['ip']}, Uptime: {proxy['upTime']:.2f}%, Latency: {proxy['latency']}ms, Protocols: {', '.join(proxy['protocols'])}"
        )

        counter += 1


if __name__ == "__main__":
    main()
