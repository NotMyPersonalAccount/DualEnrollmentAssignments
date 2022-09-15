'''
In mathematics and logic, we talk about a special function called identity.  This is a very simple function: As output, it gives whatever it was given as input, without changing anything!

Your task: create the identity function in Python.

 

We won't worry about data types for this function.  So, for example:

If it is given the int 5, it will return the int 5.

If it is given the string foo, it will return the string foo.

It's that simple!

'''

def identity(x):
	return x

print(identity(5))
print(identity("foo"))
