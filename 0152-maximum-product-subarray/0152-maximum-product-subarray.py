class Solution(object):
    def maxProduct(self, nums):
        n = len(nums)
        min_end = nums[0]
        max_end = nums[0]
        ans = nums[0]
        for i in range(1,n):
            v1 = nums[i]
            v2 = max_end * nums[i]
            v3 = min_end * nums[i]
            max_end = max(v1, max(v2,v3))
            min_end = min(v1, min(v2,v3))
            ans = max(ans, max(max_end,min_end))
        return ans
        