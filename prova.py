import requests

URL = "https://hf-api.herokuapp.com/"

risposta = requests.put(URL + "msg/1010", {"Richiesta" : "Ciao"})

print(risposta.json())