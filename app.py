from flask import Flask, url_for, render_template
from flask_restful import Api, Resource, reqparse
import json

app = Flask(__name__)

API = Api(app)

msg = reqparse.RequestParser()
msg.add_argument("Richiesta", type = str, required = True, help = "Prego inserire i dati in {Rischiesta : '...'}")

class ControlloAggiornamenti(Resource):
    def post(self, appid):
        biblio = open("data.json")
        data = json.load(biblio)
        return {appid : data[appid]}

class RisposteBorbot(Resource):
    def put(self, messaggio):
        inpt = msg.parse_args()
        return {"Risposta" : inpt['Richiesta']}

API.add_resource(ControlloAggiornamenti, "/update/<string:appid>")
API.add_resource(RisposteBorbot, "/msg/<int:messaggio>")

@app.route("/")
def home():
    return render_template("Home.html")

@app.route("/about")
def info():
    biblio = open("data.json")
    data = json.load(biblio)
    nome = data["0e448f98cbc594d8374ebecab698b4ddc08fb1ee"]["full-name"]
    versione = data["0e448f98cbc594d8374ebecab698b4ddc08fb1ee"]["current-version"]
    return render_template("about.html", nome = nome, versione = versione)


if __name__ == "__main__":
    app.run(debug=True)