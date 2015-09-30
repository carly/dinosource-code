import os
import re
import cgi
import requests
from bs4 import BeautifulSoup

					
def turn_to_soup(response_obj):
	"""Turns url Response object into a Beautiful Soup object"""
	
	soup_html = BeautifulSoup(response_obj.text)

	return soup_html


def track_element_frequencies(soup_html):
	"""Uses a python dict to track element frequencies from the
	beautiful soup object."
	
	Keys are html tags, values are frequencies in source code.
	ex. elmt_frq['div'] = 17
	"""
	
	# store element frequences in dictionary
	elmt_frq = {}
	i = 1
	
	# soup_html.find_all(True)returns a list of all soup elements
	# below function iterates through each tag and puts data into dict
	for tag in soup_html.find_all(True):
		if tag.name not in elmt_frq.keys():
			elmt_frq[tag.name] = i 
		else: 
			elmt_frq[tag.name] = elmt_frq[tag.name] + 1
					
	return elmt_frq

def cgi_escaped_html(response_obj):
	"""Given a string of html and parses so that re can work. 
	< to &lt;
	> to &gt;
	& to &amp;
	"""
	
	return cgi.escape(response_obj)
		

def add_span_class(matchobj):
	
	## code to define match obj for regex subtitution
	## trex stands for t-rex, the dinosour
	return "<span class=\"trex-{e}\">&lt;{e}".format(e=matchobj.group(1))
		
	
def add_span_tags(cgi_html):
	
	html = re.sub('&lt;([A-Z|a-z]+[0-9]*)', add_span_class, cgi_html)
	
	html = html.replace("&gt;", "&gt;</span><br>")
	
	return html
		
	