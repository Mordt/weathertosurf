from flask import Flask, jsonify
app = Flask(__name__)

"""
IDN for NSW: IDN60701
IDN for sydney coast: IDN11009

request template:
   http://www.bom.gov.au/fwo/ID<STATE>60701/ID<STATE>60701/<STATION_ID>.json

our request is:
   http://www.bom.gov.au/fwo/IDN60701/IDN60701/IDN11009.json

Information obtained from:
https://stackoverflow.com/questions/39534018/how-to-use-bom-api-for-weather-tide-and-swell

http://www.bom.gov.au/catalogue/anon-ftp.shtml



"""


@app.route("/")
def index():
    return "Hello World"

@app.route("/", methods = ["GET"])
def queryBOM():
    name = request.args.get('name')
    print name
    with open()

