'''
irst, choose an API that accepts a query string with a single parameter.

Then, write a function that takes one argument, which I'll call query_param.

Your function should make an HTTP GET request to your chosen API, and pass the query parameter that the function received as query_param.

Your function should then return the text of the HTTP response received.

 

So, for example, if your API has the following base URL: https://api.comLinks to an external site.

And expects a single query parameter called name,

And you want to hit that API, using the value michael as the query parameter for name,

You'd call the function in the following way: my_function('michael')

And your function would make an HTTP GET request to the following URL: https://api.com?name=michael

And finally, your function would return the text of the received response.
'''

import requests
import json

def predict_age(name):
	response = requests.get(f"https://api.agify.io?name={name}")
	data = json.loads(response.text)
	return data["age"]
