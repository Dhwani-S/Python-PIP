# 20CE140 - Dhwani Suthar

# You are given a string and your task is to swap cases.
# In other words, convert all lowercase letters to uppercase letters and vice versa.
# Sample Input: HackerRank.com presents "Pythonist 2".
# Sample Output: hACKERrANK.COM PRESENTS "pYTHONIST 2".

word = input("Enter the String:\t")
# ------------------------------------------------------------------------------------------------------------
# Method 1: By using swapcase()
print("Swapped Case using Method 1:", word.swapcase())

# ------------------------------------------------------------------------------------------------------------

# Method 2:
swapped = ''                            # swapped stores the final String in swapped case
for ch in word:                         # ch iterates through string 'word' character by character
    if ch.isupper():                    # isUpper() returns true if ch is in uppercase so, else returns false
        swapped = swapped+ch.lower()    # converts ch to lower case and concatenates it to the string
    else:                               # This is when ch is in lowercase
        swapped = swapped + ch.upper()  # converts ch to upper case and concatenates it to the string
print("Swapped Case using Method 2:", swapped)

# ------------------------------------------------------------------------------------------------------------

# Method 3:
swapped = ''                            # swapped stores the final String in swapped case
for ch in word:                         # ch iterates through string 'word' character by character
    swapped = swapped + ch.swapcase()   # ch converted to different case and stored in swapped
print("Swapped Case using Method 3:", swapped)

