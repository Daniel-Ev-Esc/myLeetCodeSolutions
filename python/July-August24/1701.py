class Solution(object):
    def averageWaitingTime(self, customers):
        """
        :type customers: List[List[int]]
        :rtype: float
        """
        ellapsedTime = customers[0][0]
        waitingTime = 0

        for client in customers:

            if(ellapsedTime <= client[0]):
                waitingTime += client[1]
                ellapsedTime = client[0]
            else:
                waitingTime += ellapsedTime - client[0] + client[1]
            
            ellapsedTime += client[1]

        promedioEspera = waitingTime/len(customers)

        return promedioEspera

solution = Solution()

solution.averageWaitingTime([[1,2],[2,5],[4,3]])
print(solution.averageWaitingTime([[5,2],[5,4],[10,3],[20,1]]))
print(solution.averageWaitingTime([[2,3],[6,3],[7,5],[11,3],[15,2],[18,1]]))
