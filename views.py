from flask import request, render_template
from app import app

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/sum')
@app.route('/sum/<int:x>/<int:y>')
def sum(x=None, y=None):
    return render_template('sum.html', x=x, y=y)
