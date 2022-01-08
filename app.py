from flask import Flask
from flask import request
from flask.helpers import flash
from flask.templating import render_template
from flask import url_for
import os

app = Flask(__name__)

if os.environ.get('ENV') == 'production':
    app.secret_key = os.environ.get('SECRET_KEY')
else:
    app.secret_key = 'ASSPISSSSSSSSSSSSSSSSSS'

@app.route("/")
def home():
    return render_template('home.html')

#if __name__ == "__main__":
#    app.run(host='0.0.0.0', debug=True)