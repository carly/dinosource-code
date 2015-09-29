"""dinosource code"""

#imports - standard lib
import os
import requests

#imports - flask
from flask import Flask, render_template, redirect, request, flash, session, jsonify, url_for
from flask_debugtoolbar import DebugToolbarExtension
from jinja2 import StrictUndefined
from werkzeug import secure_filename

#imports - local
from helper_functions import turn_to_soup, track_element_frequencies, add_span_tags


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
			soup_html = turn_to_soup(r)
			histogram = track_element_frequencies(soup_html)
			
			html_with_spans = add_span_tags(soup_html)
			
			print histogram
			print html_with_spans
			
			
			
			
			
	return render_template('dinosource.html', raw_html=raw_html)


if __name__ == "__main__":
	#debug=True for DebugToolbarExtension to work
	app.debug = True

	#Use the DebugToolbar
	DebugToolbarExtension(app)
	print "\n\n\n\nYO\n\n\n"
	app.run()