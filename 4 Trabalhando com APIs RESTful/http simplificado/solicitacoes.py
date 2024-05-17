import requests

reply = requests.get('http://localhost:3000')
print(reply.status_code)

if reply.status_code == requests.codes.ok:
    print("ok")

print(reply.headers)

print(reply.text)
