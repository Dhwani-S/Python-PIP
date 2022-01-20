#20CE140
# Dhwani Suthar
'''
Given the participants' score sheet for your University Sports Day, you are required to find the runner-up score. You are given n scores. Store them in a list and find the score of the runner-up.
Input Format: The first line contains. The second line contains an array A[]  of n integers each separated by a space.
'''

n = int(input("Enter size\n"))
A = [int(A) for A in input("Enter elements:\t").split()]
A.sort()
res =[]
for i in A:
    if i not in res:
        res.append(i)
print('Runner-up Score: ',res[-2])