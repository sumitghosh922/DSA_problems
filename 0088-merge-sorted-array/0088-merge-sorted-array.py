class Solution(object):
    def merge(self, nums1, m, nums2, n):
        i = m-1
        j = n-1
        id = m + n - 1
        while( i >=0 and j >=0):
            if nums1[i] >= nums2[j]:
                nums1[id] = nums1[i]
                id -=1
                i-=1
            else:
                nums1[id] = nums2[j]
                id-=1
                j-=1
        while i>=0:
            nums1[id] = nums1[i]
            id-=1
            i-=1
        while j>=0:
            nums1[id] = nums2[j]
            id-=1
            j-=1
        return nums1

            
        