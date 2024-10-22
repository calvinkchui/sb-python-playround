'''
#https://realpython.com/api-integration-in-python/
How to run demo:

> set FLASK_APP=topic\web\flask_api.py
> flask run

or
> set FLASK_APP=topic/web/flask_api.py
>  python3 -m flask --app topic/web/flask_api.py run 

'''
from flask import Flask, request, jsonify, send_from_directory
import os

app = Flask(__name__)


countries = [
    {"id": 1, "name": "Thailand", "capital": "Bangkok", "area": 513120},
    {"id": 2, "name": "Australia", "capital": "Canberra", "area": 7617930},
    {"id": 3, "name": "Egypt", "capital": "Cairo", "area": 1010408},
]

def _find_next_id():
    return max(country["id"] for country in countries) + 1

@app.get("/countries")
def get_countries():
    return jsonify(countries)

@app.post("/countries")
def add_country():
    if request.is_json:
        country = request.get_json()
        country["id"] = _find_next_id()
        countries.append(country)
        return country, 201
    return {"error": "Request must be JSON"}, 415

@app.route("/echo/<message>", methods=["GET"])
def echo(message):
    return {"message":message}

'''
@app.route("/echo_path_param/<path:message>", methods=["GET"])
def echo_path_param(message):
    return {"path_message":message}    
'''

#https://dev.to/nelsonmendezz_/how-to-create-server-files-with-flask-4hdp
@app.route('/file/<path:filename>')
def get_file(filename):
    print("filename", filename)
    print("cwd", os.getcwd())
    return send_from_directory(os.getcwd(), path=filename, as_attachment=False)



