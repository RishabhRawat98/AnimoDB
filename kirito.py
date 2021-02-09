from flask import Flask, render_template
app = Flask(__name__)

movie_info = [
    {
        'id': 1,
        'title': 'Za Waurdo',
        'description': 'Dio Brando and his gang try to stop Jotaro Kujo and the boys from smashing thier heads in',
        'Release_date': '2012'
    },
    {
        'id': 2,
        'title': 'Killer Queen',
        'description': 'My name is Yoshikage Kira',
        'Release_date': '2012'
    }
 
]





@app.route("/")
def hello():
    return render_template('home.html', movinfo = movie_info)


@app.route("/discover")
def discover():
    return "ELLO ELLO"



if __name__ == '__main__':
    app.run(debug=True)