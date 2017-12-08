import json
from flask import Flask, jsonify, render_template, request


app = Flask(__name__)


with open('s.json') as json_data:
    d = json.load(json_data)
    list_of_games = []
    for data in d['games']:
    	list_of_games.append(data)


@app.route('/', methods =['GET'])
def test():
	return render_template("index.html")

@app.route('/games', methods =['GET'])
def test1():
	return render_template("index.html",list_data=list_of_games)

@app.route('/games/<string:idd>', methods =['GET'])
def test2(idd):
	g = [game for game in list_of_games if game['id'] == idd]
	return render_template("index.html",list_data=g)

if __name__ == '__main__':
	 app.run(debug=True, host='0.0.0.0')