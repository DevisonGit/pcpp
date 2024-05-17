import requests

try:
    reply = requests.get('http://localhost:3000', timeout=1)
except requests.exceptions.Timeout:
    print("Sorry, my Mr. Impatient, you didn't get toy data")
else:
    print("Here is your data, my Master!")
