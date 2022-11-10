'''
Write a function that takes one argument, which I'll call filename. It should be assumed to be a string.

The function should open a file called filename (not the literal text "filename," but whatever is given as the argument filename) in read mode.

The function should then read the contents of the file.

The function should then close the file.

The function should then return the contents of the file, which it read earlier.

 

Note: It's okay for your function to assume that there is already a file in existence whose name matches the filename argument.  If someone uses your function to try to read from a file that doesn't exist, your function can break or crash; that's acceptable in this case.

 

Hint: Your function should open the file, then read the contents, then close the file, then return the contents that it read.  Make sure that you figure out how to do it in this order! If you try to return the file contents and then close the file, the file won't be closed because a function stops executing as soon as you return something from it!
'''

def read_file(filename):
    file = open(filename, "r")
    contents = file.read()
    file.close()
    return contents