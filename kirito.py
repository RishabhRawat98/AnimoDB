from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm
app = Flask(__name__)

app.config['SECRET_KEY'] ='IDK'

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
def home():
    return render_template('home.html', movinfo = movie_info)


@app.route("/discover")
def discover():
    return render_template('discover.html')






@app.route("/register", methods=["Get", "POST"])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', page_name='Register', form=form)

@app.route("/login")
def login():
    form = LoginForm()
    return render_template('login.html', page_name='Login', form=form)








if __name__ == '__main__':
    app.run(debug=True)