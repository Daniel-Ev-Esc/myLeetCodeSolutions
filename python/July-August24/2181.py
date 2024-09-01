# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def mergeNodes(self, head):
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

        sum = 0

        previousNode = None
        head = initialList[0]

        finalList = []

        while head.next != None:
            sum += head.val

            if head.next.val == 0:
                currentNode = ListNode(sum)
                sum = 0
                if previousNode != None:
                    previousNode.next = currentNode

                finalList.append(currentNode)

                previousNode = currentNode
            head = head.next

        #for node in finalList:
           # print(node.val,end=",")
        return finalList

solution = Solution()

solution.mergeNodes([0,1,0,3,0,2,2,0])
solution.mergeNodes([0,3,1,0,4,5,2,0])
