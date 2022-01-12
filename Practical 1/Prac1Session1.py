#Prac 3 11/01/22
#Conditionals

### If condition
# a=3
# if a>0:
#     print('A is a positive number')
# else:
#     print('This is a negative number')

#Odd or even
# print('Find odd or even')
# a=6
# b=3
# if b%2==0:
#     print('Even')
# else:
#     print('Odd')
#
# if a>0:
#     print('a i =s positive number')
# elif a<0:
#     print('a is negative')
# else:
#     print('a is 0')

# a = 0
# if a>0 and a%2 == 0:
#     print('a is even and positive')
# elif a>0 and a%2!=0:
#     print('a is positive')
# elif a==0:
#     print('a is 0')

# user = 'James'
# access=3
# if user == 'admin' or access >=4:
#     print('Access Granted!')
# else:
#     print('Access denied')




#Exercise 1:
# print('Enter your age: ')
# age = input()
# if int(age) >= 18:
#     print('Feedback: You\'re old enough to drive')
# else:
#     print('Feedback: Please wait for ',18- int(age),' years')

#Excercise 2:
# my_age = 19
# print('Enter you age: ')
# your_age = int(input())
# if(my_age > your_age):
#     if(my_age-your_age > 1):
#         print('I am ',my_age-your_age, ' years older than you')
#     else:
#         print('I am 1 year older than you')
# elif(your_age > my_age):
#     if(your_age - my_age >1):
#         print('You are ',your_age - my_age,' years older than me')
#     else:
#         print('You are 1 year older than me')
# else:
#     print('We are of same age!')
#
#
# #3.
# print('Enter first number: ')
# num1 = input()
# print('Enter the second number: ')
# num2 = input()
# if(num1>num2):
#     print(num1,'is greater than ',num2)
# elif(num2 > num1):
#     print(num2,'is greater than ',num1)
# else:
#     print(num1,' is equal to ',num2)


#Loops
#while
# count = 0
# while count<5:
#     print(count)
#     count=count+1
# else:
#     print(count)

#Break
# count = 0
# while count < 5:
#     print(count)
#     count = count +1
#     if count == 3:
#         break

# count = 0
# while count < 5:
#     if count == 3:
#         continue
#     print(count)
#     count = count + 1


#For loop
# language = 'Python'
#
# for letter in language:
#     print(letter)
#
# for i in range(len(language)-2):
#     print(language[i])

# person = {
#     'first_name':'Dhwani',
#     'last_name':'Suthar',
#     'age':19,
#     'country':'India',
#     'is_married':False,
#     'skills':['Wire wrap','Concept art','Oil Painting','Python'],
#     'address':{
#         'address line 1':'Sec 9,171/A',
#         'Township':'RIL',
#         'City':'Jamnagar',
#         'State':'Gujarat',
#         'zipcode':'361142'
#     }
# }
# # for key in person:
# #     print(key)
#
# for key, value in person.items():
#     print(key,' : ',value)

#Range
# lst = list(range(11))
# print(lst)
# lst = list(range(0,11,2))
# print(lst)
# st = set(range(0,11,2))
# print(st)
#
# lst1 = list(range(-3,12,2))
# print(lst1)
# lst2 = list(range(-10,-2,2))
# print(lst2)


#Nested Loop
person = {
    'first_name':'Dhwani',
    'last_name':'Suthar',
    'age':19,
    'country':'India',
    'is_married':False,
    'skills':['Wire wrap','Concept art','Oil Painting','Python'],
    'address':{
        'address line 1':'Sec 9,171/A',
        'Township':'RIL',
        'City':'Jamnagar',
        'State':'Gujarat',
        'zipcode':'361142'
    }
}

# for key in person:
#     if key == 'address':
#         for address in person['address']:
#             print(address)

# for number in range(11):
#     print(number)
# else:
#     print('The loop stops at', number)






#Exercises: Level 1
#Even
#2.
print('2: \n')
for i in range(10,-1,-1):
    print(i)

# 4.
print('\n\n4: \n')
print('Enter a num')
n = int(input())
str = ''
for i in range(0,n):
    for j in range(0,n):
        str = str+' # '
    print(str)
    str = ''

#6.
print('\n\n6: \n')
lst = ['Python', 'Numpy','Pandas','Django', 'Flask']
for item in lst:
    print(item)

#8.
print('\n\n7: \n')
print('Printing only odd numbers')
for i in range(0,101):
    if i%2 !=0:
        print(i)


#Level 2:
#1.
print('\n\n1: \n')
sum =0
for i in range(0,101):
        sum += i
print('Sum: ',sum)



#2.
print('\n\n2: \n')
esum=0
osum=0
for i in range(0,101):
    if i%2 == 0:
        esum+=i
    else:
        osum+=i
print('Odd sum: ',osum,'\nEven Sum: ',esum)

