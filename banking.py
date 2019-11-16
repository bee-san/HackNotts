import requests
import json
request = requests.get("http://localhost:9876/api/customer/accounts")
print(request.json())