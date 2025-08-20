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

