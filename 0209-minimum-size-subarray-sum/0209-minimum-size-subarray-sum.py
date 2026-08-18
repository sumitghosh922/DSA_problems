class Solution(object):
    def minSubArrayLen(self, target, nums):
        low = 0
        res = float('inf')
        sum = 0
        for high in range(len(nums)):
            sum = sum + nums[high]
            while(sum>=target):
                if high == len(nums):
                    break
                length = high - low+1
                res = min(res,length)
                sum = sum - nums[low]
                low+=1
        if res == float('inf'):
            return 0
        else:
            return res

    

        