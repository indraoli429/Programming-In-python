#!/usr/bin/python

print("A or + : Add or B or * : Multiplication or C or /: Division")

num1 = int(input("Enter First Number: "))

num2 = int(input("Enter Second Number: "))

choice = input("What do you want to do: ")

print('Choice is: '+choice)

multiply = num1 * num2
addition = num1 + num2
division = num1 / num2

if choice =="M" or choice =="m":
	print("This is multiply")
	print(multiply)

elif choice =="A" or choice =="a":
	print("This is adding")
	print(addition)

elif choice =="D" or choice =="d":
	print("This is Division")
	print(division)
else: print("no answer")
