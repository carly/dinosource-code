"""dinosource code"""

#imports - standard lib
import os
import pprint

#imports - flask
from flask import Flask, render_template, redirect, request, flash, session, jsonify, url_for
from flask_bootstrap import Bootstrap
from flask_debugtoolbar import DebugToolbarExtension

#imports - 3rd party
from jinja2 import StrictUndefined
from werkzeug import secure_filename

#imports - local


#app config
app = Flask(__name__)

printer = pprint.PrettyPrinter()

app.secret_key="""SuperSecret"""
app.jinja_env.undefined = StrictUndefined


@app.route('/')
def index():
	"""renders index.html - homepage"""
	
	return render_template('index.html')

@app.route('/source-code')
def source_code():
	"""renders view with source code and tag summary."""
	
	return render_template('dinosource.html')

if __name__ == "__main__":
	#debug=True for DebugToolbarExtension to work
	app.debug = True
	connect_to_db(app)

	#Use the DebugToolbar
	DebugToolbarExtension(app)
	print "\n\n\n\nYO\n\n\n"
	app.run()