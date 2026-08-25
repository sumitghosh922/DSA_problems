class Solution(object):
    def maximumSum(self, arr):
        noDel = arr[0]
        oneDel = float('-inf')
        result = arr[0]
        for i in range(1,len(arr)):
            previousNoDel = noDel
            noDel = max(noDel+arr[i],arr[i])
            oneDel = max(oneDel+arr[i],previousNoDel)
            result = max(result,noDel,oneDel) 
        return result

