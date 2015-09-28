"""dinosource code"""

#imports - standard lib
import lxml.html
import os
import re
import requests

#imports - flask
from flask import Flask, render_template, redirect, request, flash, session, jsonify, url_for
from flask_debugtoolbar import DebugToolbarExtension

#imports - 3rd party
from bs4 import BeautifulSoup
from jinja2 import StrictUndefined
from werkzeug import secure_filename

#imports - local


#app config
app = Flask(__name__)

app.secret_key="""SuperSecret"""
app.jinja_env.undefined = StrictUndefined


@app.route('/')
def index():
	"""renders index.html - homepage"""
	
	return render_template('index.html')


@app.route('/parse-url', methods=["GET", "POST"])
def parse_url():
	"""tbd"""
	
	if request.method == "POST":
		# get url that person has entered
		try: 
			url = request.form.get("parse-url")
			r = requests.get(url)
			
		except (requests.exceptions.ConnectionError, requests.exceptions.InvalidURL):
			flash('Roar. Invalid URL or Connection Error. Try again plz.')
			return redirect('/')
		
		if r: 
			
			# use beautiful soup to parse
			raw_html = BeautifulSoup(r.text)
			source_code = raw_html.prettify(formatter=None)
			
			# dictionary to track tag frequency
			tag_dict = {}
			i = 1
			for tag in raw_html.find_all(True):
				if tag.name not in tag_dict.keys():
					tag_dict[tag.name] = i 
				else: 
					tag_dict[tag.name] = tag_dict[tag.name] + 1
					
			print tag_dict
			
			
	return render_template('dinosource.html', source_code=source_code)


if __name__ == "__main__":
	#debug=True for DebugToolbarExtension to work
	app.debug = True

	#Use the DebugToolbar
	DebugToolbarExtension(app)
	print "\n\n\n\nYO\n\n\n"
	app.run()