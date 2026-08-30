class Solution(object):
    def removeDuplicates(self, nums):
        unique = 1
        n=len(nums)
        i = 0
        j = 1
        while(j<n):
            if nums[j] == nums[j-1]:
                j+=1
                continue
            else:
                i+=1
                nums[i] = nums[j]
                j+=1
                unique+=1
        return unique
        