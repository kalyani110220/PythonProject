#conditional expression = A one-line shortcut for the  if-else statement(ternary operator)
#                      Print or assign  one of two values based on a condition
#                        X if  condition else y
num = 6

#print ("Positive" if num > 0 else "Negative")
result = "Even" if num % 2 == 0 else "Odd"
print(result)