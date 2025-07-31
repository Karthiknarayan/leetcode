#
# @lc app=leetcode id=643 lang=python3
#
# [643] Maximum Average Subarray I
#

# @lc code=start
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        #this is a fixed size wwindow so calculate for first window

        #1.calculate avg for first window
        windowsum=sum(nums[:k])
        windowavg=windowsum/k
        maxavg=windowavg

        #2.slide the window
        for i in range(k,len(nums)):
            windowsum=windowsum+nums[i]-nums[i-k]
            windowavg=windowsum/k
            maxavg=max(windowavg,maxavg)

        return maxavg

# @lc code=end

