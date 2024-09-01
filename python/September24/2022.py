# 01/09/24
# 2022. Convert 1D Array Into 2D Array
# https://leetcode.com/problems/convert-1d-array-into-2d-array/description/

class Solution(object):
    def construct2DArray(self, original, m, n):
        """
        :type original: List[int]
        :type m: int
        :type n: int
        :rtype: List[List[int]]
        """
        # A better way to do this is m*n == len(original) but i want to keep the solution as i got it
        if m*n < len(original) or len(original)/n < m:
            return []
        
        # The main idea is to build the subarrays and add them to the main array whrn n elements are inserted
        twoDimensionalArray = []
        internalList = []

        j = 0

        for element in original:
            internalList.append(element)
            j+=1
            if j == n:
                twoDimensionalArray.append(internalList)
                # Reset the pointer and subarray
                internalList = []
                j=0

        return twoDimensionalArray

solution = Solution()

print(solution.construct2DArray([1,2,3,4], 2,2))
print(solution.construct2DArray([1,2,3], 1,3))
print(solution.construct2DArray([1,2], 1,1))