"""dinosource code server"""

#imports - standard lib
import os
import requests

#imports - flask
from flask import Flask, render_template, redirect, request, flash, jsonify, Markup
from flask_debugtoolbar import DebugToolbarExtension
from jinja2 import StrictUndefined

#imports - local
from helper_functions import turn_to_soup, track_element_frequencies, cgi_escaped_html, add_span_tags


#app config
app = Flask(__name__)


app.secret_key="""DinosourWhispers"""
app.jinja_env.undefined = StrictUndefined


@app.route('/')
def index():
	"""renders index.html - homepage"""
	
	return render_template('index.html')


@app.route('/parse-url', methods=["GET", "POST"])
def parse_url():
	"""Takes url from index.html form, returns source code. 
	
	Parses source code to create summary table, and clean 
	source code view.
	"""
	
	if request.method == "POST":
		# get url that person has entered
		try: 
			url = request.form.get("parse-url")
			html = requests.get(url)
			
		except (requests.exceptions.ConnectionError, requests.exceptions.InvalidURL):
			flash('Roar. Invalid URL or Connection Error. Try again plz.')
			return redirect('/')
		
		if html: 
			
			# code to create summary table
			soup_html = turn_to_soup(html)
			summary = track_element_frequencies(soup_html)
			
			# prep html for display 
			html_to_encode = html.text
			cgi_html = cgi_escaped_html(html_to_encode)
			source_code = Markup(add_span_tags(cgi_html))
			
			website_url = url[7:]
				
	return render_template('dinosource.html', summary=summary, source_code=source_code, website_url=website_url)




if __name__ == "__main__":
	#debug=True for DebugToolbarExtension to work
	app.debug = True

	#Use the DebugToolbar
	DebugToolbarExtension(app)
	print "\n\n\n\nYO\n\n\n"
	app.run()