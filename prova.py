import requests

URL = "http://127.0.0.1:5000/"

risposta = requests.post(URL + "update/0e448f98cbc594d8374ebecab698b4ddc08fb1ee")

print(risposta.json())