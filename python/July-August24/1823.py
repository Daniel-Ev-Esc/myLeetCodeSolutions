class Solution(object):
    def findTheWinner(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """

        def calculateWinner(n,k):
            if n == 1:
                return 0
            return (calculateWinner(n-1,k) + k)%n

        return calculateWinner(n,k) + 1
        
solution = Solution()

print(solution.findTheWinner(5,2))
print(solution.findTheWinner(6,5))