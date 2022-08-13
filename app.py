from crypt import methods
from flask import Flask, render_template, request
import requests

URL = "https://api.openbrewerydb.org/breweries/"

app = Flask(__name__)



@app.route('/', methods = ['GET'] )
def home():
    result = requests.get(URL, verify=False)
    breweries = result.json()

    return render_template('index.html',breweries=breweries)



@app.route('/', methods = ['POST'] )
def get_data():
    data = request.form['city']
    city_name = data.replace(" ","_")
    parameters = {
        "by_city":city_name.lower()
        }
    result = requests.get(URL,params=parameters, verify=False)
    breweries = result.json()

    return render_template('index.html',breweries=breweries)



if __name__ == '__main__':
    app.run(debug=True, port=8080)
