import json
import requests 

data = {
    "profile": "jelambrar",
    "is_active": True
}

try:
    res = requests.get(url="http://localhost:5000/api/add_profile", data=json.dumps(data))
    # res = requests.get(url="http://localhost:5000/")
except requests.RequestException:
    print("Error")

print(res.status_code)
