import common
import routes
from flask import Flask
from flask_restplus import Api

app = Flask(__name__)
api = Api(app)


@app.route("/index")
def index():
    user = {'nome': 'Arthur', 'idade': 21, 'curso': 'Sistemas de infromação'}

    return routes.index(user)


@app.route("/version")
def getversion():
    return common.getversion()


@app.route("/status")
def getstatus():
    return common.getstatus()
