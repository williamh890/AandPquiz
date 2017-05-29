from flask import Flask

#setup the flask app
app = Flask(__name__)
app.config.from_pyfile('config.py')

#import all the views
from views import *

if __name__ == '__main__':
    app.run(debug=True)
