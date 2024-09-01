# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def passThePillow(self, n, time):
        """
        :type n: int
        :type time: int
        :rtype: int
        """
        movesToEnd = n-1

        finalIndex = time%movesToEnd
        reverse = (time//movesToEnd)%2 != 0

        if reverse:
            return n - finalIndex 
        else:
            return finalIndex + 1



solution = Solution()

print(solution.passThePillow(4,5))
print(solution.passThePillow(3,2))
print(solution.passThePillow(9,4))

