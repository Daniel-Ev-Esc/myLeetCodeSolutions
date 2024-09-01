class Solution(object):
    def minOperations(self, logs):
        """
        :type logs: List[str]
        :rtype: int
        """

        distance = 0
        for log in logs:
            if(log == "../"):
                if(distance > 0):
                    distance -= 1
            elif log != "./":
                distance += 1
        
        return distance
        

solution = Solution()

print(solution.minOperations(["d1/","d2/","../","d21/","./"]))
print(solution.minOperations(["d1/","../","../","../"]))
print(solution.minOperations(["d1/","d2/","./","d3/","../","d31/"]))
print(solution.minOperations(["./","../","./"]))
