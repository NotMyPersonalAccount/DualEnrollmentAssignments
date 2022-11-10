'''
Write a function that takes two arguments, which I'll call filename and string.  Both should be assumed to be strings.

The function should open a file called filename (not the literal text "filename," but whatever is given as the argument filename) in write mode.

The function should then write the argument string to the file.

The function should then flush the write buffer, close the file, and finish.

The function should not return anything!
'''

def write_file(filename, string):
    file = open(filename, "w")
    file.write(string)
    file.flush()
    file.close()