from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "ZA WAURDO.........TOKI WO TOMARE"


@app.route("/discover")
def discover():
    return "ELLO ELLO"



if __name__ == '__main__':
    app.run(debug=True)