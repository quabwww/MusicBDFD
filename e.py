import requests
json = {"user_id": "487430318500872203", 
        "channel_id": "1117201886836162630", 
        "guild_id": "1077968892535775262", 
        "query": "tv gir not allowed"}
url  = requests.post(f"http://localhost:8000/play-music/", json=json)

print(url.json())