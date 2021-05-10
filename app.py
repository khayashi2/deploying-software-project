import requests
from flask import Flask
from main import hello_message

FORTNITE_API = 'https://fortnite-api.com/v1/stats/br/v2'


app = Flask(__name__)

@app.route('/')
def hello():
    message = ''
    message += hello_message("Kaleo")
    params = {'format': 'json'}
    response = requests.get(FORTNITE_API + '5e70c11741254facbdbf36b88971f1b6', params=params)
    if response.status_code == 404:
        message += "\nIt seems you have not played a game of fornite"
    else:
        message += "\nThere is stat available on your fortnite account"


    return message


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')