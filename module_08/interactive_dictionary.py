'''
Create an empty dictionary.  Then, welcome the user and give the user a menu with the following options:

Add a key-value pair to the dictionary.
Remove a key-value pair from the dictionary.
Quit.
Make sure that each choice does what's intended, then return to this main menu and do it again.

Print the dictionary after each choice is done!
'''

'''
Welcome to SmartDictionary!
Currently, the dictionary is empty.

Do you want to (a)dd a kv pair, (r)emove a kv pair, or (q)uit? a
What key do you want to add? name
What is the value for this key? Oakland Tech
Currently the dictionary is as follows: {'name': 'Oakland Tech'}

Do you want to (a)dd a kv pair, (r)emove a kv pair, or (q)uit? a
What key do you want to add? school_type
What is the value for this key? High School
Currently the dictionary is as follows: {'name': 'Oakland Tech', 'school_type': 'High School}

Do you want to (a)dd a kv pair, (r)emove a kv pair, or (q)uit? r
What key do you want to remove? name
Currently the dictionary is as follows: {'school_type': 'High School'}

Do you want to (a)dd a kv pair, (r)emove a kv pair, or (q)uit? q
'''

dict = {}

print("Welcome to SmartDictionary")
print("Currently, the dictionary is empty.")
print()
while True:
    action = input("Do you want to (a)dd a kv pair, (r)emove a kv pair, or (q)uit? ")
    if action == "q":
        break
    elif action == "a":
        key = input("What key do you want to add? ")
        value = input("What is the value for this key? ")
        dict[key] = value
    elif action == "r":
        key = input("What key do you want to remove? ")
        del dict[key]
    else:
        continue
    print(f"Currently the dictionary is as follows: {dict}")
