import requests
json = {"user_id": "487430318500872203", 
        "channel_id": "1117201886836162630", 
        "guild_id": "1077968892535775262", 
        "query": "zoe azul"}

url  = requests.post("https://musicbdfd.onrender.com/play-music/", json=json)

print(url.text)