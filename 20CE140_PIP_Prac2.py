#20CE140 Dhwani Suthar
#Python Practical 2

###Dictionary###

#a. Write a Python script to check whether a given key already exists in a dictionary.
d1 = {"20CE140":"Dhwani", "20CE146":"Kavya", "20CE150":"Medha"}
print("Enter a Key:")
keys = input()
if keys in d1:
    print("Key exists")
else:
    print("key does not exist")


#b. Write a Python script to merge two Python dictionaries.
d1 = {"20CE140": "Dhwani", "20CE146": "Kavya", "20CE150": "Medha"}
d2 = {"20CS024": "Dikshita"}
#d1= d1+d2
d1.update(d2)
print(d1)


#c. Write a Python program to sum all the items in a dictionary.
price = {"Pen": 10, "Eraser": 5, "Books": 200}
list = []
for i in price:
    list.append(price[i])
total= sum(list)
print("Total: ",total)

#d. Write a Python script to add a key to a dictionary.
#Sample Dictionary : {0: 10, 1: 20}
#Expected Result : {0: 10, 1: 20, 2: 30}
d1 = {"20CE140": "Dhwani", "20CE146": "Kavya", "20CE150": "Medha"}

print("Enter a key you want to add: ")
keys = input()
print("Enter the corresponding value: ")
values = input()
d1[keys] = values
print(d1)


#e. Write a Python script to concatenate following dictionaries to create a new one.

#Sample Dictionary :
#dic1={1:10, 2:20}
#dic2={3:30, 4:40}
#dic3={5:50,6:60}
#Expected Result : {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}

dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50,6:60}
dic1.update(dic2)
dic1.update(dic3)
print(dic1)


###Tuple###

#a. Write a Python program to create a tuple with different data types.
tp1 = ('item1', 'item2', 'item3',4,5, 1.1);
print(tp1)

#b. Write a Python program to create a tuple with numbers and print one item.
tpnum = (1,2,3,4,5,6,7,8,9)
print('Number at index 1: ',tpnum[1])

#c. Write a Python program to add an item in a tuple.
tpnum = tpnum + (10,)   #This will create a new tuple with original values and 10 at the end
print(tpnum)

#d. Write a Python program to convert a tuple to a string.
tp2 = ('d','h','w','a','n','i')
str = ''
for item in tp2:
    str = str + item
print('String: ',str)

#e. Write a Python program to find the length of a tuple.
tp3 = ('d','h','w','a','n','i')
print(len(tp3))


###Set###

#a. Write a Python program to add member(s) in a set and clear a set
st1 = {1,2,3,4,5,6,7,8}
st1.add(9)
print("Set 1: ",st1)
#clearing the set:
st1.clear()
print(st1)

#b. Write a Python program to remove an item from a set if it is present in the set.
# st1.remove(('item1'))  #not present so it won't be removed
st1 = {1,2,3,4,5,6,7,8,9}
st1.remove(9)
print(st1)


#c. Write a Python program to create an intersection, Union, difference of sets.
st1 = {0, 2, 4, 6, 8}
st2 = {1, 2, 3, 4, 5}
print("intersection :", st1 & st2)
print("union: ", st1|st2)
print("difference :", st1-st2)


#d. Write a Python program to find maximum and the minimum value in a set.
st1 = {0, 2, 4, 6, 8}
print('max: ',max(st1))
print('min: ', min(st1))


#e. Write a Python program to find the most common elements and their counts from list, tuple, dictionary
#list
lst = ['first','second','first','third','first','second','second','second']
count = 0
element = lst[0]
for i in lst:
        ctr = lst.count(i)
        if(ctr > count):
            count = ctr
            element = i
print(element)

#tuple
tp = ('first','second','first','third','first','second','second','second')
count = 0
element = tp[0]
for i in tp:
        ctr = tp.count(i)
        if(ctr > count):
            count = ctr
            element = i
print(element)

#dictionary
dic = {'1':1, '2':2,'3':3,'4':4,'5':2,'1':2}
tp = tuple(dic.values())
count = 0
element = tp[0]
for i in tp:
        ctr = tp.count(i)
        if(ctr > count):
            count = ctr
            element = i
print(element)