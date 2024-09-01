# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def numWaterBottles(self, numBottles, numExchange):
        """
        :type numBottles: int
        :type numExchange: int
        :rtype: int
        """
        total = numBottles

        while numBottles >= numExchange:
            drink = numBottles // numExchange
            numBottles = drink + numBottles%numExchange
            total += drink

        return total
        

solution = Solution()

print(solution.numWaterBottles(9,3))
print(solution.numWaterBottles(15,4))

