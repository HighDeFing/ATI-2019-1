from flask import Flask, flash, redirect, render_template, request, session, abort
import os

app = Flask(__name__)


@app.route('/home.html')
def home(name=None):
    if not session.get('logged_in'):
        return render_template('home.html', name='home.html')
    elif session.get('logged_in'):
        return "Hello " + request.form['username']


@app.route('/login', methods=['POST'])
def do_user_login():
    if request.form['password'] == '1234' and request.form['username'] == 'heider':
        session['logged_in'] = True
    else:
        flash('wrong password')
    return home()


if __name__ == "__main__":
    app.secret_key = os.urandom(12)
    app.run(host='0.0.0.0', port=80)
