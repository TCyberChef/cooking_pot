"""Intro to Python - Part 1 - Hands-On Exercise."""


import math
import random


print("TODO: Write a print statement that displays both the type and value of `pi`")
print("")
pi = math.pi
print(type(pi))
print(pi)
print("")

print("TODO: Write a conditional to print out if `i` is less than or greater than 50")
print("")
i = random.randint(0, 100)
print("The random generated num is {}".format(i))
if i > 50:
    print("This Number Is greater than 50")
elif i < 50:
    print("This Number Is Less Than 50")
print("")

print("TODO: Write a conditional that prints the color of the picked fruit")
print("")
picked_fruit = random.choice(['orange', 'strawberry', 'banana'])
if picked_fruit == "orange":
    print("The color of your fruit is orange")
elif picked_fruit == "banana":
    print("The color of your fruit is Yello")
else:
    print("The color of your fruit is Red")
print("")

# TODO: Write a function that multiplies two numbers and returns the result
# Define the function here.
def kefel(num1, num2):
    return num1*num2


print("TODO: Now call the function a few times to calculate the following answers")
print("")

print("12 x 96 =",kefel(12,96))

print("48 x 17 =",kefel(48,17))

print("196523 x 87323 =",kefel(196523,87323))
