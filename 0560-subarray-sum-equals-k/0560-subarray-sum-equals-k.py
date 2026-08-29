class Solution(object):
    def subarraySum(self, nums, k):
        f = {0:1}
        total = 0
        count = 0
        for i in nums:
            total+=i
            needed = total - k
            count+= f.get(needed,0)
            f[total] = f.get(total,0) + 1
        return count
            
        