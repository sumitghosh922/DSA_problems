class Solution(object):
    def subarraysDivByK(self, nums, k):
        count = 0
        total = 0
        f = {0:1}
        for i in range(len(nums)):
            total +=nums[i]
            rem = total%k
            if rem < 0:
                rem += k
            count += f.get(rem,0)
            f[rem] = f.get(rem,0)+1
        return count
        