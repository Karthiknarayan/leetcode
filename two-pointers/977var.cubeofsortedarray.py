nums=[-7,-3,2,3,11]
def sortedSquares(nums):
        for i in range(len(nums)):
            nums[i]=nums[i]*nums[i]*nums[i]
        
        # 16,1,0,9,100
        res=[0]*len(nums)
        i=len(nums)-1
        l=0
        r=len(nums)-1
        for i in range(len(nums)-1, -1,-1):
            if nums[l]>=nums[r]:
                res[i]=nums[l]
                l+=1

            else:
                res[i]=nums[r]
                r-=1
        return res

print(sortedSquares(nums))