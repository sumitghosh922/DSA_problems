class Solution(object):
    def removeDuplicates(self, s):
        res = ""
        stack=[]
        for i in range(len(s)):
            if len(stack)==0:
                stack.append(s[i])
                continue
            if stack[-1] == s[i]:
                stack.pop()
                continue
            stack.append(s[i])
        for i in stack:
            res+=i
        # res.reverse()
        return res
        