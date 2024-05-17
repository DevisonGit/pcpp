import requests


#  Mostra os coddigos de status
for k, v in requests.codes.__dict__.items():
    print(k, v)
