# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def nodesBetweenCriticalPoints(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """

        initialList= []

        previousNode = ListNode(head[0])
        initialList.append(previousNode)
        
        for i in range(1,len(head)):
            node = ListNode(head[i])
            previousNode.next = node

            initialList.append(node)
            previousNode = node

        head = initialList[0]

        distancesArray = [-1,-1]

        count = 0

        distanceMin = 0
        distanceMax = 0

        while head.next.next != None:
            if count >= 1:
                    distanceMax += 1
                    distanceMin += 1
            if (head.next.val < head.val and head.next.val < head.next.next.val) or (head.next.val > head.val and head.next.val > head.next.next.val):
                count += 1
                
                if count >= 2:
                    if distancesArray[0] == -1:
                        distancesArray[0] = distanceMin
                    elif distanceMin < distancesArray[0]:
                        distancesArray[0] = distanceMin

                    if distancesArray[1] < distanceMax:
                        distancesArray[1] = distanceMax
                    
                    distanceMin = 0
            head = head.next
            
        return distancesArray

solution = Solution()

solution.nodesBetweenCriticalPoints([3,1])
solution.nodesBetweenCriticalPoints([5,3,1,2,5,1,2])
solution.nodesBetweenCriticalPoints([1,3,2,2,3,2,2,2,7])
