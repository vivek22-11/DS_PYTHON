
with open('pi_digits.txt') as file_object:
    contents = file_object.read() 
print(contents)



'''rstrip() method remove or strips any whitespace'''

with open('pi_digits.txt') as file_object:
    contents = file_object.read() 
print(contents.rstrip())



#Relative path and absolute path
''' "c:/Data Science/pi_digits.txt" (absolute path) '''

file_path = "C:/Data Science/pi_digits.txt"
with open(file_path) as file_object:
    contents = file_object.read() 
print(contents.rstrip())


'''read line by line'''
filename= 'pi_digits.txt'
with open(filename) as file_object:
    for line in file_object:
        print(line)


filename= 'pi_digits.txt'
with open(filename) as file_object:
    for line in file_object:
        print(line.rstrip())
        

filename= 'pi_digits.txt'
with open(filename) as file_object:
    lines= file_object.readlines()
for line in lines:
    print(line.rstrip())
    


filename = 'programming.txt'
with open (filename,'w') as file_object:
    file_object.write("hiii,I Love Programming")



filename = 'programming.txt'
with open (filename,'w') as file_object:
    file_object.write("I Love Programming")
    file_object.write("I love creating new games.")
    
    
filename = 'programming.txt'
with open (filename,'w') as file_object:
    file_object.write("I Love Programming.\n")
    file_object.write("I love creating new games.\n")


'''Appending to a file'''

filename = 'programming.txt'
with open (filename,'a') as file_object:
    file_object.write("I also Love finding meaning in .\n")
    file_object.write("I love creating new apps that can run.\n")

