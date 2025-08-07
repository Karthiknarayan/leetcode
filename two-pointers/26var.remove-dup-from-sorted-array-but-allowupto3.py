# 🔸 Problem Statement:
# You're given a sorted array.
# Modify it in-place so that each unique element appears at most 3 times.

# Return the new length of the array after removal.
# All remaining elements should be at the beginning of the array.

# ✅ Examples:
# 📘 Example 1:
# python
# Copy
# Edit
# Input:  nums = [1,1,1,1,2,2,3]
# Output: [1,1,1,2,2,3]
# Length: 6
# 🟢 Explanation:

# 1 appears 4 times → keep only 3

# 2 appears 2 times → keep both

# 3 appears once → keep it

# 📘 Example 2:
# python
# Copy
# Edit
# Input:  nums = [0,0,0,0,1,1,1,1,2,3,3,3,3]
# Output: [0,0,0,1,1,1,2,3,3,3]
# Length: 10
# 🟢 Explanation:

# 0 appears 4 → keep 3

# 1 appears 4 → keep 3

# 2 appears once → keep

# 3 appears 4 → keep 3

# 📘 Example 3:
# python
# Copy
# Edit
# Input:  nums = [5,5,5,5,5]
# Output: [5,5,5]
# Length: 3
# 🟢 Explanation: Only 5 is there, and it appears 5 times → keep first 3.

# 📘 Example 4:
# python
# Copy
# Edit
# Input:  nums = [1,2,3]
# Output: [1,2,3]
# Length: 3
# 🟢 Explanation: All unique values. No duplicates to remove.
 
a=[5,5,5,5,5]
def removeDupKeep3(a):
    count=0
    i=0
    j=0
    for j in range(len(a)):
        if a[i-1]==a[j] and i>0:
            if count<3:
                count+=1
                a[i]=a[j]
                i+=1 
                
        elif a[i]!=a[j] or i==0:
            count=1
            a[i]=a[j]
            i+=1

    print(i)

removeDupKeep3(a)
