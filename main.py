#Exercise 1 : Write a program that greets you by your own name.
'''''
name = input("Enter your name: ")

if name == "Nare":
    print("Hello, Nare!")

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


'''''
"""""
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


"""""
'''''
#Exercis 6
import random

three_randoms = ''.join([str(random.randint(0, 9)) for _ in range(3)])
print(f"3-digit code: {three_randoms}")

four_randoms =''.join([str(random.randint(1, 6)) for _ in range(4)])
print(f"4-digit code: {four_randoms}")

'''
'''
i = 1
while i < 11:
    print(i)
    i = i + 1
'''
'''''
greeting = int(input("How many greetings do you want to display"))
first_greeting = 0
while first_greeting < greeting:
    print("good Morning")
    first_greeting = first_greeting + 1
    
'''

''''
command = input("Enter command:")
while command != "stop":
    print("Executing command")
    command = input("enter command")
    print("execution is stopped")

'''
''''
import random

dice1= dice2= rolls= 0
while (dice1 != 6 or dice2 !=6):
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)
    rolls +=1
    print(f"The dices was rolled {rolls:d} times")
    
'''
''''
command = input("enter command: ")
while command!="stop":
    if command=="MAYDAY":
        break
        print ("exectuing command:")
        command = input("Enter command: ")
        print ("Execution stopped")
'''
''''
import random
hid_no = random.randint(1,100)
player_guess = 0
while not player_guess == hid_no:
    player_guess = int(input("Guess a number"))
    if player_guess > hid_no:
        print("Too high")
    elif player_guess < hid_no:
        print("You are close but too low")
    else: player_guess = 100
    print("nice")
'''
import math

''''
while True:
    number = int(input("Please type a number"))
    if number <= 0:
        break

    factorial = 1
    new = 1
    while new <= number:
            factorial *= new
            new += 1
    print(f"The factorail is {number} is {factorial}")
print("thanks and bye")
'''
''''
import math

number = 1

while number <= 1000:

    if number % 3 == 0:
        print(number)

    # Increment the number
    number += 1
'''

'''''
# Conversions
total_pounds = (talents * POUNDS_PER_TALENT) + pounds
total_lots = (total_pounds * LOTS_PER_POUND)
total_grams = total_lots * GRAMS_PER_LOT

# Calculate kilograms and grams
kilograms = float(total_grams // 1000)
grams = float(total_grams % 1000)
'''''
'''''
Inches_percm = 3.4
Centimeters_perinch = 0,35

value = float(input("Enter distance you want to convert in inches"))

conversion = value * Centimeters_perinch
if conversion <=0:
    print("negative value")
'''
''''
scores = [85, 92, 78, 61, 45, 99, 72, 88]

for score in scores:
    if score >= 90:
        print(f"Your grade {score} is A")
    elif score >= 80 and score <= 89:
        print(f"Your grade {score} is B")
    elif score >= 70 and score <= 79:
        print(f"Your grade {score} is C")
    elif score >= 60 and score <= 79:
        print(f"Your grade {score} is D")
    else:
        print(f"Your grade {score} is F")

print("All done")

'''

while True:
    value = int(input("Enter a number: "))

    if value < 0:
        print("Negative value entered. Terminating the program.")
        break


    print(f"You entered a positive value: {value}")


