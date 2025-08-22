# Exercise1 Rectangle Area Clac


length = float(input("Enter the length: "))
width = float(input("Enter the width: "))
area = length * width
print(f"The area of {length} x {width} is {area}cm2")

#  Exercise 2 Shopping Cart Program
item = input("What item you would like to buy?: ")
price = float(input("Enter the price: "))
quantity= int(input("Enter the quantity: "))
total = price * quantity
print(f"You have bought {quantity} of {item} at {total}.")
print(f"The total price is {total}")

# Exercise 3 circumference of a circle

import math
radius=float(input("Enter the radius: "))
circumference= 2 * math.pi * radius
print(f"The circumference  is {round(circumference,2)}cms")

# Exercise 4 Area of circle

import math
radius=float(input("Enter the radius: "))
area = math.pi * radius ** 2
print(f"The area of {radius} x {radius} is {area}cm2")

#Excercise 5 the hypotenuse of a right or right-angled triangle

import math
a=float(input("Enter the a: "))
b=float(input("Enter the b: "))
c= math.sqrt(pow(a,2)+pow(b,2))
print(f"The area of {a} x {b} is {c}cm2")

#python calculator

operator = input("Enter an operator(+ - * /): ")
number1 = float(input("Enter the number: "))
number2 = float(input("Enter the number: "))
if operator == "+":
    print(number1 + number2)
elif operator == "-":
    print(number1 - number2)
elif operator == "*":
    print(number1 * number2)
elif operator == "/":
    print(number1 / number2)
else:
    print("Invalid operator")

#python weight converter

weight = float(input("Enter the weight: "))
unit= input("kilograms or Pounds?(K or L): ")
if unit == "K":
 print(weight * 2.205)
elif unit == "L":
    print(weight / 2.205)
else:
    print("Invalid unit")






