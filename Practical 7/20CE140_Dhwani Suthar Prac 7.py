# Dhwani Suthar - 20CE140
# Lapindrome is defined as a string which when split in the middle, gives two halves having the same characters and same
# frequency of each character. If there are odd number of characters in the string, we ignore the middle character and
# check for lapindrome. For example gaga is a lapindrome, since the two halves ga and ga have the same characters with
# same frequency. Also, abccab, rotor and xyzxy are a few examples of lapindromes. Note that abbaab is NOT a lapindrome.
# The two halves contain the same characters but their frequencies do not match. Your task is simple.
# Given a string, you need to tell if it is a lapindrome.

n = int(input("Enter number of input from the user: "))
for i in range(0, n):
    word = input("Enter the word: ")
    first = word[0:len(word) // 2]    # first half of the word is stored in word
    if len(word) % 2 == 0:        # if the word is of even length,
        second = word[len(word) // 2:]  # the second half : from the very next character to the end of the string
    else:  # else if the length is odd,
        second = word[len(word) // 2 + 1:]  # the middle character is to be skipped
    lst1 = list(first)  # store the first word as list
    lst2 = list(second)  # store the second word as list
    lst1.sort()  #sorting the words
    lst2.sort()
    first = str(lst1)
    second = str(lst2)
    if first == second:  # if the first half is identical to the second
        print('YES')  # the string is a lapindrome
    else: # else,
        print('NO')  # it is not a lapindrome
        