'''
Write a function that takes one argument, which I'll call url.

Your function should make an HTTP GET request to that url, and return the text of the response.
'''

import requests

def http_get(url):
	response = requests.get(url)
	return response.text
