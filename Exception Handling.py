'''the error signifies a situation that mostly
happen due to the absence of system resources
the exceptiona are the issues that can appear
at runtime and compile time
it majorly arises in the code or program
authored by the developers.

Exception are handled with try-except block
Handling the ZeroDivisionError exception
'''

print(5/0)

#using try-except Block
try:
   print(5/0)
except ZeroDivisionError:
    print("You can't divide by zero")

    
''' Handling errors correctly is especially
important when the program has
more work to do 
invalid input appropriately,
it can prompt for more vaild input
instead of crashing
'''

print("Give me two numbers and i'll divide them.")
print("enter 'q' to quit.")
while True:
    first_number = input("\n First number: ")
    if first_number =='q':
        break
    second_number = input("\n Second number: ")
    if second_number=='q':
        break
    answer = int(first_number) / int (second_number)
    print(answer)
    

'''handling the FileNotFoundError Exception'''

filename ='alice.txt' 
with open(filename,encoding = 'utf-8') as f:
    content = f.read()
    

filename ='a.txt' 
with open(filename,encoding = 'utf-8') as f:
    content = f.read()
 
    
filename ='alice.txt'
try:
    with open(filename,encoding = 'utf-8') as f:
        content = f.read()
except  FileNotFoundError:
    print(f"sorry,the file{filename} does not exist")


filename ='a.txt'
try:
    with open(filename,encoding = 'utf-8') as f:
        content = f.read()
except  FileNotFoundError:
    print(f"sorry,the file{filename} does not exist")
    