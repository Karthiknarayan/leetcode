#
# @lc app=leetcode id=209 lang=python3
#
# [209] Minimum Size Subarray Sum
#

# @lc code=start
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left=0
        curlen=0
        cursum=0
        minlen=float('inf')
#this is a variable sized sliding window
        totalsum=sum(nums[:])
        if totalsum<target:
            return 0
        for i in range (len(nums)):
            cursum+=nums[i]

            while cursum>=target:
                minlen=min(minlen,i-left+1)
                cursum-=nums[left]
                left+=1          
        if target==0:
            return 0
        else:
            return minlen
            
                

        
# @lc code=end

