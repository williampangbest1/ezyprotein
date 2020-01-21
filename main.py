import flask
from pair_search import pair_search,pairs_search 
import json

app = flask.Flask(__name__)

@app.route("/")
def myhome():
	return flask.render_template("home.html")

@app.route("/aboutus")
def myaboutus():
	return flask.render_template("aboutus.html")

@app.route("/home")
def myIndex():
	return flask.render_template("index.html")


@app.route('/home', methods=['POST'])
def search():
	#s = flask.request.values["data"];
	s=flask.request.get_json();
	s=s["data"];
	a=pairs_search(s[0],float(s[1]["value"]));
	
	results=pair_search(s);
	#return flask.render_template("index.html", result=json.dumps(result))
	return json.dumps(a)

if __name__ == "__main__":
	app.run(debug=True)