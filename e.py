import requests
json = {"user_id": "487430318500872203", 
        "channel_id": "1117201886836162630", 
        "guild_id": "1077968892535775262", 
        "query": "tv gir not allowed"}
req = "https://f1bf012d-c513-4256-8dae-351f7622d10e-00-124jjeazni7de.worf.replit.dev"
if not req:
    print("none")
url  = requests.post("https://f1bf012d-c513-4256-8dae-351f7622d10e-00-124jjeazni7de.worf.replit.dev/play-music/", json=json)

print(url.json())