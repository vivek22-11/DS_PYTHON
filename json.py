#storing data
''' many of your programs will ask user to 
input certain kinds of information.
you might allow users to store preferences
in a game or provide
such as list and dictionaries.
when users close a program,
you'll almost always want to save
A simple way to do this involves 
storing your data using the
json module
'''
#JSON (Javascript Object Notation)

'''json.dump() and json.load()'''
import json
numbers=[2,3,5,7,11,13]
filename= 'numbers.json'
with open(filename,'w') as f:
    json.dump(numbers, f)
    


import json
username = input(" what is your name ? ")
filename= 'username.json'
with open(filename,'w') as f:
    json.dump(username, f)
print(f" we'll remeber you when you come back ,{username}!")



import json
filename= 'username.json'
with open(filename) as f:
    username= json.load(f)
print(f"welcome back, {username}!")



import json
filename= 'username.json'
try:
    with open(filename) as f:
        username= json.load(f)
except FileNotFoundError:
    username = input(" what is your name ? ")
    with open(filename,'w') as f:
        json.dump(username, f)
        print(f" we'll remeber you when you come back ,{username}!")
else:
    print(f"welcome back, {username}!")
