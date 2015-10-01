# dinosource-code

Have you seen the dinosaurs? Have you seen source code? No idea...? Never fear //dinosource-code is here.
//dinosource-code enables users to analyze the underlying html structure of their favorite websites. 
 

![alt tag](https://raw.github.com/carly/dinosource-code/master/static/img/dino2.jpg)

<h3>Instructions:</h3>
Simply enter a URL, and a friendly dinosour will perform the following magic: <br>
- Display the "source code" of the requested URL. <br>
- Generate a table detailing the frequency of each HTML element for a given webpage.<br>
- Highlight a table element and its corresponding appearances in the html upon mouseclick.</p>

![alt tag](https://raw.github.com/carly/dinosource-code/master/static/img/highlightdino.jpg)

<h3>Technology Stack:</h3>
- Python
- Flask
- JavaScript/jQuery
- BeautifulSoup
- Regular Expressions
- CGI
- Bootstrap


<h3>Getting to the Source Code | The Scrape </h3>
To fetch and parse HTML from a url for analysis, I used a combination of Python's 'requests', <br>
'BeautifulSoup', 're', and 'cgi' libraries. The user's url input is sent to the server, and <br>
passed to the 'requests' .get() function which returns an html Response object.

<h3>Getting to the Source Code | The Parse </h3>

After checking to make sure the url is valid, the parse_url() function performs two operations on the Response object:

1. Creates a histogram style table to track element frequencies
	- Helper functions: 
		- Generate a Beautiful Soup object
		- Use BeautifulSoup's find_all method to count element frequencies
		- Return a python dictionary that tracks elements and frequencies in given source code 

2. Prepare the source code for clean display and jQuery interaction
	- Helper functions: 
		- Takes same response object from first step and passes it to a cgi_escape function to prep for regex
		- Uses Python regex to add a span tag that corresponds to each element in the html
			- jQuery uses span class to toggle the highlight class on elements 
		- Adds breaks to opening tags to return a readable source code display.
		
		
<h3>Challenges</h3>
The greatest challenge was figuring out how to wrap each element in the html with a customized span tag. 
First, I tried using BeautifulSoup's wrap() method. However, after experiencing extremely slow render time and 
realizing the added spans will only behave as Markup if the inital html response was properly encoded, I started 
looking at other options. After reading documentation on lxml, ElementSoup, CGI and Regex, I decided to use CGI 
and Regex over BeautifulSoup to add spans after considering factors of relative ease of implementation and efficiency. 

<h4>Future Improvements</h4>

- Implement the table as a barchart with d3js to add tooltips, and ability to sort by frequency
		
