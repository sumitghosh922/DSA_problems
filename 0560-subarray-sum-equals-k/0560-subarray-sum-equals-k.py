class Solution(object):
    def subarraySum(self, nums, k):
        count =0
        f = {0:1}
        total = 0
        for i in range(len(nums)):
            total+=nums[i]
            needed = total - k
            count+=f.get(needed,0)
            f[total] = f.get(total,0)+1
        return count
            
            
        