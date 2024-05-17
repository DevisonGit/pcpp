import requests

try:
    reply = requests.get('http:////////////', timeout=1)
except requests.exceptions.InvalidURL:
    print("Recipient unknown!")
else:
    print("Everything fine!")
