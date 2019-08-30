"""Login mongo db application."""
from flask import Flask, url_for, redirect, render_template, request, session
from flask_pymongo import PyMongo
import bcrypt

APP = Flask(__name__)

APP.config['MONGO_DBNAME'] = 'mongo_login_db'
APP.config['MONGO_URI'] = 'mongodb://localhost:27017/users_db'

MONGO = PyMongo(APP)


@APP.route('/')
def index():
    """
    Index route.
    :return: index page.
    """
    if 'username' in session:
        return 'Yoy are logged in as {}'.format(session['username'])

    return render_template('index.html')


@APP.route('/login', methods=['POST'])
def login():
    """
    Sign in route.
    :return: index page or error message.
    """
    users = MONGO.db.users
    login_user = users.find_one({'name': request.form['username']})
    if login_user:
        if bcrypt.hashpw(request.form['pass'].encode('utf-8'),
                         login_user['password']) == login_user['password']:
            session['username'] = request.form['username']
            return redirect(url_for('index'))
    return 'Invalid username/password combination.'


@APP.route('/register', methods=['POST', 'GET'])
def register():
    """
    Sign up route.
    :return: index page or error message.
    """
    if request.method == 'POST':
        users = MONGO.db.users
        existing_user = users.find_one({'name': request.form['username']})

        if existing_user is None:
            hashpass = bcrypt.hashpw(request.form['pass'].encode('utf-8'), bcrypt.gensalt())
            users.insert({'name': request.form['username'], 'password': hashpass})
            session['username'] = request.form['username']
            return redirect(url_for('index'))

        return 'This user already exists!'

    return render_template('register.html')


if __name__ == '__main__':
    APP.secret_key = 'mysecretkey'
    APP.run(debug=True)
