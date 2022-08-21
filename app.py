import os
from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')
def index():
	return render_template('index.html')


@app.route('/aboutme')
def abtme():
	return render_template('aboutme.html')


if __name__ == "__main__":
	app.run(debug=True, host="127.0.0.1", port=80)