import requests

try:
    reply = requests.get('http://localhost:3000/cars', timeout=1)
except requests.RequestException:
    print('Communication Error')
else:
    if reply.status_code == requests.codes.ok:
        print(reply.text)
    else:
        print('Server error')
