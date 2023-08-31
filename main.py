#Exercise 1 : Write a program that greets you by your own name.

name = input("Enter your name: ")

if name == "Egzon":
    print("Hello, Egzon!")

#Exercise 1, with two Names
name = input("Enter your name: ")

if name == "Egzon":
    print("Hello, Egzon!")
elif name == "John":
    print("Hello, John!")



# Exercise 2 : Write a program that asks the user for the radius of a circle and the prints out the area of the circle.

import math

radius = float(input("Enter radius of the circle : "))
area = math.pi * (radius ** 2)
print("Surface is", area)




# Exercise 3 : Write a program that asks the user for the length and width of a rectangle. The program then prints out the perimeter and area of the rectangle. The perimeter of a rectangle is the sum of the lengths of each four sides.

import math
width = float(input("Enter the width of the rectangle:"))
length = float(input("Enter the length of the rectangle:"))
perimeter = width + length * 2
print("Perimeter is:", perimeter)




#Exercise 4 : Write a program that asks the user for three integer numbers. The program prints out the sum, product, and average of the numbers.

import math
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))

sum_nums = num1 + num2 + num3
product_nums = num1 * num2 * num3
average_nums = sum_nums / 3

print("Sum:", sum_nums)
print("Product:", product_nums)
print("Average:", average_nums)

# Exercise 5 :Write a program that asks the user to enter a mass in medieval units: talents (leiviskä), pounds (naula), and lots (luoti). The program converts the input to full kilograms and grams and outputs the result to the user:

# One talent is 20 pounds.
# One pound is 32 lots.
# One lot is 13,3 grams.




POUNDS_PER_TALENT = 20
LOTS_PER_POUND = 32
GRAMS_PER_LOT = 13.3

talents = float(input("Enter mass in talents: "))
pounds = float(input("Enter mass in pounds: "))
lots = float(input("Enter mass in lots: "))

# Conversions
total_pounds = (talents * POUNDS_PER_TALENT) + pounds
total_lots = (total_pounds * LOTS_PER_POUND)
total_grams = total_lots * GRAMS_PER_LOT

# Calculate kilograms and grams
kilograms = float(total_grams // 1000)
grams = float(total_grams % 1000)

print(f"The equivalent mass is {kilograms} kilograms and {grams} grams.")

