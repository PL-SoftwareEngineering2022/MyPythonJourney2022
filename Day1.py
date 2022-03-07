#Define what you want your program to do:
    #what is the input, what goes into the code or program?
    #what is the output?
#Write pseudo code about the program: this is just an outline in a human listing the steps that you should take for your program to run.
#Write the code: implement the code

# Write a program that collects a passowrd and a username, and checks if that information is correct.
# The program greets you and gives you access into the account.
    #write the pseudo code:
    #ask the user for their name
    #ask for their password
    #check the name and the password
    #greet and grant access if there is a match
    #otherwise, let them know that their password or username is invalid
name = input("Enter you name: ")
password = input("Enter your password: ")

if name=="John" and password=="123":
    print(f"Hi {name}, Welcome to Landmark")
else: 
    print("Hi, Your username or password is incorrect.")


Enter you name: Mark
Enter your password: 123
Hi, Your username or password is incorrect.
name = input("Enter you name: ")
password = input("Enter your password: ")

if name=="John" and password=="123":
    print(f"Hi {name}, Welcome to Landmark")
else: 
    print("Hi, Your username or password is incorrect.")
    
Enter you name: John
Enter your password: 123
Hi John, Welcome to Landmark


# write a program that calculates the area:
length = 10
width = 5
area = length*width
print(area)
50

def area(length, width):
    return length*width
area(10, 5)
50
def area(length, width):
    return length*width
area(356, 27)
9612
