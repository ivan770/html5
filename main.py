from flask import Flask
from flask import render_template
from flask import request
from pathlib import Path
app = Flask(__name__)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('index.html')

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run()
