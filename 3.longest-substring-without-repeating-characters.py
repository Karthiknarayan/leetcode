#
# @lc app=leetcode id=3 lang=python3
#
# [3] Longest Substring Without Repeating Characters
#

# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left=0
        seen=set()
        maxlen=0

        for i in range (len(s)):
            while s[i] in seen:
                seen.remove(s[left])
                left+=1


            seen.add(s[i])
            maxlen=max(maxlen,i-left+1)
        return maxlen




# Given a string s, count how many substrings of length k have all unique characters.

# Input:
# s = "abcabc", k = 3
# Output:
# 3 → ("abc", "bca", "cab")


# @lc code=end

