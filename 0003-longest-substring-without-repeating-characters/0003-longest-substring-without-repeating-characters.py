class Solution(object):
    def lengthOfLongestSubstring(self, s):
        res = 0
        low = 0
        freq={}
        n = len(s)
        for high in range(n):
            freq[s[high]] = freq.get(s[high],0)+1
            k = high-low+1
            while(len(freq) < k):
                freq[s[low]]-=1
                if freq[s[low]]==0:
                    del freq[s[low]]
                low+=1
                k = high-low+1
            length = high-low+1
            res = max(length,res)
        return res
        