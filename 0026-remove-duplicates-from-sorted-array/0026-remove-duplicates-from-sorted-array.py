class Solution(object):
    def removeDuplicates(self, nums):
        start = 0 
        cm = 1
        unique = 1
        while(cm < len(nums)):
            if nums[cm] == nums[cm-1]:
                cm+=1
                continue
            else:
                unique+=1
                start+=1
                nums[start] = nums[cm]
                cm+=1
        return unique
        