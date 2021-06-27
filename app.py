from flask import Flask
from flask_restful import Api, Resource, reqparse

app = Flask(__name__)

API = Api(app)

msg = reqparse.RequestParser()
msg.add_argument("Richiesta", type = str, required = True, help = "Prego inserire i dati in {Rischiesta : '...'}")

class ControlloAggiornamenti(Resource):
    def get(self):
        return {"Build" : "alfa 0.01"}

class RisposteBorbot(Resource):
    def put(self, messaggio):
        inpt = msg.parse_args()
        return {"Risposta" : inpt['Richiesta']}

API.add_resource(ControlloAggiornamenti, "/update")
API.add_resource(RisposteBorbot, "/msg/<int:messaggio>")

@app.route("/")
def home():
    return ("Ciao da HF")

if __name__ == "__main__":
    app.run()