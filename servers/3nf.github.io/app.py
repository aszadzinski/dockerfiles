from flask import Flask

app = Flask(__name__)
app.debug = True

@app.route("/")
def test():
	return "TEST!!"

if __name__=="__main__":
	app.run(host="0.0.0.0")
