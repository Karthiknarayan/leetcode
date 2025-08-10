# Problem statement
# Given a string s, reverse only the consonant letters in the string and keep all vowels and non-letter characters (spaces, punctuation, digits) in their original positions. Return the resulting string.

# Vowels: a, e, i, o, u (treat both uppercase and lowercase as vowels).

# Consonants: any English alphabet letter that is not a vowel.

# Preserve case of every character (i.e., don't change letter case), only move consonants.

# Input
# A string s (may contain letters, digits, punctuation, spaces).
# Example constraints (suggested):

# 0 <= len(s) <= 10^5

# s contains ASCII characters.

# Output
# A new string where consonants are reversed in order, while vowels and non-letter characters remain at their original indices.

# Examples
# Example 1

# vbnet
# Copy
# Edit
    # Input:  "hello"  lelho
    # Output: "olleh"
    # Explanation: consonants are h, l, l → reversed → l, l, h. Vowel 'e' stays in place.
    # Resulting string: "olleh"
    # Example 2

# vbnet
# Copy
# Edit
# Input:  "a-bC-dEf-ghIj"_-bc-d_f-gh_j
# Output: "a-jIh-dEf-Cb-"
# Explanation:
# Letters: a b C d E f g h I j
# Vowels: a, E, I stay where they are.
# Consonants (in order): b, C, d, f, g, h, j  → reversed: j, h, g, f, d, C, b
# Place them back into consonant slots.
# Example 3

# vbnet
# Copy
# Edit
# Input:  "123, xyz!"
# Output: "123, zyx!"
# Explanation: digits and punctuation unchanged. Consonants x,y,z reversed to z,y,x.
# Example 4

# vbnet
# Copy
# Edit
# Input:  ""
# Output: ""
# Explanation: empty string stays empty.


s="aieouxyz        123"  
def reverseeveryexceptvovel(s):
    i=0
    j=len(s)-1
    s=list(s)

    vowel=['a','e','i','o','u',' ', ]
    #both are not vowel
    #i is vowel, j is not vowel
    # i is not vowel, j is not vowel
    # i is vowel, j is vowel
    #i is not vowel j is vowel
    while i<=j:
        if s[i] in vowel or not s[i].isalpha():
                i+=1

        if s[j] in vowel  or not s[j].isalpha():
               j-=1

        elif s[i] not in vowel  or not s[i].isalpha() and s[j]  not in vowel or not s[j].isalpha():
            s[i],s[j]=s[j],s[i]
            i+=1
            j-=1

    print("".join(s))

reverseeveryexceptvovel(s)