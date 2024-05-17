import requests

try:
    reply = requests.get('http://localhost:3001', timeout=1)
except requests.exceptions.ConnectionError:
    print("Nobody's home, sorry!")
else:
    print("Everything fine!")
