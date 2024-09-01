class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        aux = 0
        if len(nums2) > 0:
            numToInsert = nums2.pop()
            for i in range(len(nums1)):
                if nums1[i] >= numToInsert:
                    aux = nums1[i]
                    nums1[i] = numToInsert
                    numToInsert

                


solution = Solution()

solution.merge([1,2,3,0,0,0],3, [2,5,6], 3)
solution.merge([1],1, [], 0)

