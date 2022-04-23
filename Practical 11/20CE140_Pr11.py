# 20CE140 - Dhwani Suthar
# ----------------------------------------------------------------------------------------------------------------------

# You are given a string. Your task is to count the frequency of letters of the stri ng and
# pri nt the letters in descendi ng order of frequency.
# If the foll owi ng string is gi ven as input to the progra m:
# aabbbccde
# Then, the out put of the progra m shoul d be:
# b 3
# a 2
# c 2
# d 1
# e 1

# str1 = input("Enter a String\n")
# res = {}
#
# for keys in str1:
#     res[keys] = res.get(keys, 0) + 1
# for keys,value in sorted(res.items()):
#     print(keys, value)

# ----------------------------------------------------------------------------------------------------------------------

# Write a procedure to find min,  max,  mean, standard  deviation,  variance  of  number list.\
# Example
# Input :  10  50  80  70  49  23  11  4
# output :  4  80  37. 13  27. 25  848. 70

# import statistics
#
# elements = [int(elements) for elements in input("\nEnter: ").split()]
# min = min(elements)
# max = max(elements)
# print("min : ",min,"\nmax : ",max)
# sum=0
# for i in elements:
#     sum=sum+i
# mean = sum/len(elements)
# print("mean: ",mean)
# print("Standard deviation: ","{:.2f}".format(statistics.stdev(elements)))
# print("Variance: ","{:.2f}".format(statistics.variance(elements)))

# ----------------------------------------------------------------------------------------------------------------------

# You are given an integer array height of length n. There are n vertical lines drawn such
# that the two endpoints of the ith line are (i, 0) and (i, height[i]).
# Find two lines that together with the x-axis for m a container, such that the container
# contains the most water.
# Return the maximum amount of water a container can store.
# Notice that you may not slant the container.
# Input: height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
# Output: 49
# Explanation: The above vertical lines are represented by array [1, 8, 6, 2, 5,4, 8, 3, 7]. In
# this case, the max area of water (blue section) the container can contain is 49.
# Example 2:
# Input: height = [1, 1]
# Output: 1

# tank = [int(tank) for tank in input("\nEnter heights: ").split()]
# tank.sort()
# capacity = set(tank)
#
# print("Contains: ",list(capacity)[-2]*list(capacity)[-2])

# ----------------------------------------------------------------------------------------------------------------------

# Given a list of integers, write a program to print the count of all possible unique
# combinations of numbers whose sum is equal to K.
# Input
# The first line of input will contain space-separated integers.
# The second line of input will contain an integer, denoting K.
# Output
# The output should be containing the count of all unique combinations of numbers
# whose sum is equal to K.
# Sample Input 1
# 2 4 6 1 3
# 6
# Sample Output 1
# 3

# from itertools import combinations
# values = [int(values) for values in input("Enter values: ").split()]
# values.sort()
# k = int(input("Enter K: "))
# count = 0
# for i in range(1, len(values)+1):
#     temp = set(combinations(values, i))
#     com = list(temp)
#     for combination in com:
#         if sum(combination) == k:
#             count += 1
# print(f"Total Combinations of sum {k} is: ", count)

# ----------------------------------------------------------------------------------------------------------------------

# Explain about the different types of Exceptions in Python with suitable example.

# Built-in exceptions
# try:
#     a = 10/0
#     print(a)
# except ArithmeticError:
#         print("This is an Exception. 20CE140 - Dhwani Suthar")
# else:
#     print("Success! No exception")
#
#
# try:
#     a = [140, 240, 340]
#     print(a[3])
# except LookupError:
#     print("Index out of bound error. 20CE140 - Dhwani Suthar")
# else:
#     print("Success! No exception")
#
# try:
#     a = int(input ("enter value\t="))
#     b = 10/a
#     print(b)
# except ZeroDivisionError:
#     print("ZeroDivisionError")
# except:
#     print("something went wrong")
#
# # Finally
# a = 10
# try:
#   print(a)
# except:
#   print("Something went wrong")
# finally:
#   print("hello c# corner")
#
# # Raise
# a = 1000#a value is above 100
# if 100 < a:
#   raise Exception("Sorry, the numbers above 100")

# ----------------------------------------------------------------------------------------------------------------------

# Complete django tutorial (part 1 to part 7) from the official document.
# https://docs.djangoproject.com/en/4.0

# ----------------------------------------------------------------------------------------------------------------------

# Python program to demonstrate
# method overriding

# class Parent():
#
#     def __init__(self):
#         self.value = "Inside Parent - 20CE140"
#
#     def display(self):
#         print(self.value)
#
#
# class Child(Parent):
#
#     def __init__(self):
#         self.value = "Inside Child - 20CE140"
#
#     def display(self):
#         print(self.value)
#
# obj1 = Parent()
# obj2 = Child()
#
# obj1.display()
# obj2.display()

# ----------------------------------------------------------------------------------------------------------------------

# Write Python code to create a function named move_rectangle() that takes an object
# of Rectangle class and two numbers named dx and dy. It should change the location of
# the Rectangle by adding dx to the x coordinate of corner and adding dy to they
# coordinate of corner
class Point(object):
    ""
class Rectangle(object):
    ""

def move_rectangle(rect, dx, dy):
    rect.corner.x += dx
    rect.corner.y += dy

box = Rectangle()
box.width = 100.0
box.height = 200.0
box.corner = Point()
box.corner.x = 0.0
box.corner.y = 0.0

print(box.corner.x)
print(box.corner.y)

move_rectangle(box, 3.0, 3.0)

print(box.corner.x)
print(box.corner.y)