class Solution(object):
    def construct2DArray(self, original, m, n):
        """
        :type original: List[int]
        :type m: int
        :type n: int
        :rtype: List[List[int]]
        """

        if m*n < len(original) or len(original)/n < m:
            return []

        twoDimensionalArray = []
        internalList = []

        j = 0

        for element in original:
            internalList.append(element)
            j+=1
            if j == n:
                twoDimensionalArray.append(internalList)
                internalList = []
                j=0

        return twoDimensionalArray

solution = Solution()

print(solution.construct2DArray([1,2,3,4], 2,2))
print(solution.construct2DArray([1,2,3], 1,3))
print(solution.construct2DArray([1,2], 1,1))