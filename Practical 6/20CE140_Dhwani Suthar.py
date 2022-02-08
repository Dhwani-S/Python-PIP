# 20CE140 - Dhwani Suthar
# AIM: You are given n words. Some words may repeat. For each word, output its number of occurrences.
# The output order should correspond with the input order of appearance of the word. See the sample input/output for
# clarification.
# Sample Input
# 4
# bcdef
# abcdefg
# bcde
# bcdef
# Sample Output
# 3
# 2 1 1
# Explanation: There are 3 distinct words. Here, "bcdef" appears twice in the input at the first and last positions.
# The other words appear once each. The order of the first appearances are "bcdef", "abcdefg" and "bcde" which
# corresponds to the output.

words = {}
n = int(input("Enter total number of words to be entered\t"))  # n is total number of words
for i in range(n):  # 0<=i<n
    ele = input("Enter String: ")
    if ele not in words:  # if the string is not present in words
        words[ele] = 1
    else:
        words[ele] = words.get(ele, 0) + 1  # if the string is already present then increment the value
print(len(words))  # words contain all the words as keys only once
for value in words.values():
    print(value, end=' ')

