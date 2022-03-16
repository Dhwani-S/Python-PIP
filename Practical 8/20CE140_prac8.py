# 20CE140 - Dhwani Suthar
# Write a Program in Python to implement a Stack Data Structure using Class and Objects, with push, pop, and traversal
# method.
class stack:
    def __init__(self):
        self.item=[]

    #push
    def push(self,data):
        self.item.append(data)

    #pop function
    def pop(self):
        return self.item.pop()

    #traversal
    def traversal(self):
        for i in self.item:
            print(i,end=" ")

s1=stack()
s1.push(11)
s1.push(21)
s1.push(31)
print("Traversed: ")
s1.traversal()
print('\n')
s1.push(41)
print('Popped: ',s1.pop())
print('Popped: ',s1.pop())
s1.push(51)
print("Printing the element --> ")
s1.traversal()
