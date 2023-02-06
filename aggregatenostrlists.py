import requests
import json

urls = [
    "https://dpinkerton.com/.well-known/nostr.json",
    "https://rogue.earth/.well-known/nostr.json",
    "https://nostrplebs.com/.well-known/nostr.json",
    "https://nostrverified.com/.well-known/nostr.json",
    "https://getalby.com/.well-known/nostr.json",
    "https://nostr.directory/.well-known/nostr.json",
    "https://no.str.cr/.well-known/nostr.json",
    "https://bitcoinnostr.com/.well-known/nostr.json",
    "https://nip05.nostr.band/.well-known/nostr.json",
    "https://nostr.com.au/.well-known/nostr.json",
    # Add more URLs as needed
]

aggregated_data = {"names": {}}

for i, url in enumerate(urls, 1):
    print(f"Downloading data from {url} ({i}/{len(urls)}):", end=" ")
    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            aggregated_data["names"].update(data["names"])
            print("100.00%")
        else:
            print("Failed")
    except requests.exceptions.RequestException as e:
        print("Failed")

with open("aggregated_data.json", "w") as f:
    json.dump(aggregated_data, f)