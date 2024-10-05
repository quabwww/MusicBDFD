import requests
id = 1100148368996573265
json = {"user_id": "487430318500872203", 
        "channel_id": "1117201886836162630", 
        "guild_id": "1077968892535775262", 
        "query": "azul - zoe"}
url  = requests.post(f"http://localhost:8000/play-music/", json=json)

print(url.json())