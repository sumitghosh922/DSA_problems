class Solution(object):
    def maxAbsoluteSum(self, nums):
        min_sum = max_sum = nums[0]
        curr_min = curr_max = nums[0]
        res = nums[0]
        for i in range(1,len(nums)):
            curr_min = min(curr_min+nums[i],nums[i])
            curr_max = max(curr_max+nums[i],nums[i])
            min_sum = min(min_sum,curr_min)
            max_sum = max(max_sum,curr_max)
            res = max(res,abs(min_sum),abs(max_sum))
        return abs(res)
        