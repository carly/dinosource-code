import lxml.html
import os
import re
import requests

from bs4 import BeautifulSoup			
					
def turn_to_soup(request_obj):
	"""Turns url Response object into a Beautiful Soup object"""
	
	soup_html = BeautifulSoup(request_obj.text)
	
	return soup_html


def track_element_frequencies(soup_html):
	"""Uses a python dictionary to generate a histogram of element 		frequencies.
	
	Keys are html tags, values are frequencies in source code.
	ex. histogram['div'] = 17
	"""
	
	# store element frequences in dictionary
	e_fr = {}
	
	i = 1
	for tag in soup_html.find_all(True):
		if tag.name not in e_fr.keys():
			e_fr[tag.name] = i 
		else: 
			e_fr[tag.name] = e_fr[tag.name] + 1
					
	return e_fr
	
def add_span_tags(soup, e_dict):
	"""Adds <span> tags to each html element, so jQuery can target.
	
	Takes in the soup_html from turn_to_soup().
	Uses BeautifulSoup wrap() to add span tags to all elements in 		soup_html.
	"""
	
	# histogram dict with elements as keys, get list of keys
	elements = e_dict.keys()
	
	span_tag = soup.new_tag("span")
	
	for e in elements: 
		soup.find_all(e)
		
		
		
		
	for tag in soup: 
		soup.tag.wrap(add_span)
		soup.span['class'] = 'tag'
		
	return soup
		
		
	