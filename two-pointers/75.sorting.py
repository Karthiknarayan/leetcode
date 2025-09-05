def sortColors(nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(len(nums)):
            for j in range(i,len(nums)):
                if nums[i]>=nums[j]:
                    temp=nums[i]
                    nums[i]=nums[j]
                    nums[j]=temp

nums=[1,2,0,2]
sortColors(nums)
print(nums)




