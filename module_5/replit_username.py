'''
When you use Replit.com, you're seeing the results of a Python process running on a remote Replit.com server.

This challenge is to use Python's standard library to determine the name of the user on the Replit server's operating system who "owns" the process!

Hint:  The Replit.com server in which your process is running is a "Unix-like" operating system.
'''

from subprocess import PIPE, Popen

user = Popen(args="whoami", stdout=PIPE, shell=True).communicate()[0].decode("utf-8").strip()
print(user)
