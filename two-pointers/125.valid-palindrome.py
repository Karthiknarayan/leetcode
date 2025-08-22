# 125. Valid Palindrome
# Solved
# Easy
# Topics
# premium lock icon
# Companies
# A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

# Given a string s, return true if it is a palindrome, or false otherwise.

 

# Example 1:

# Input: s = "A man, a plan, a canal: Panama"
# Output: true
# Explanation: "amanaplanacanalpanama" is a palindrome.
# Example 2:

# Input: s = "race a car"
# Output: false
# Explanation: "raceacar" is not a palindrome.
# Example 3:

# Input: s = " "
# Output: true
# Explanation: s is an empty string "" after removing non-alphanumeric characters.
# Since an empty string reads the same forward and backward, it is a palindrome.


s="amma,:"
def Validpalin(s):
    news=""
    for i in range(len(s)):
        if s[i].isalpha() or s[i].isdigit() or s[i]==" ":
            news+=s[i].lower()

    l=0
    r=len(news)-1
    #to reverse each word and store back in the same aray
    while l<=r:
        if news[l]!=news[r]:
            return False
        l+=1
        r-=1
    return True


print(Validpalin(s))

        

