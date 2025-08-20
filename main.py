#This is my first Python Program
print("I like Pizza")
print("I don't like Pizza")
#variable = A container for a value(string,integer,float,boolean)
#           A variable behaves as if it was the value it contains
#String
first_name = "Kalyani"
food = "puri"
email = "kalyani133@gmail.vom"
print(f"Hello {first_name}")
print(f" You like {food} ")
print(f" Your email is {email} ")
#Integers
age = 32
quantity = 12
num_of_students = 30
print(f"I am {age} years old")
print(f"you are buying {quantity} items")
print(f"you class has {num_of_students} students")
# Float
price = 10.99
print(f"price is £{price}")
# Boolean
is_student = True
for_sale = True
if for_sale:
    print("You are a sale")
else:
        print("You are not a sale")
# Typecasting = the process of converting   a variable from one data type to another
# str(),int(),float(),bool()
name = "Kalyani"
age=32
gpa = 3.2
is_student=False
name = bool(name)
print(name)
# input =  A function that prompts the user to enter data
#        Returns the entered data as a string
name = input ("What is your name?")
age = input ("How old are you?")
age = int(age)
age =age + 2
print(f"Hello {name} ")
print ("HAPPY BIRTHDAY")
print(f"You are {age} years old")