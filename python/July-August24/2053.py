class Solution(object):
    def kthDistinct(self, arr, k):
        """
        :type arr: List[str]
        :type k: int
        :rtype: str
        """

        stringDict = dict()

        for stri in arr:
            if not stri in stringDict:
                stringDict[stri] = 1
            else:
                stringDict[stri] += 1
        
        distinct = [string for string in arr if stringDict[string] == 1]
          
        if len(distinct) >= k:
            return distinct[k-1]
        else:
            return ""



        
solution = Solution()

print(solution.kthDistinct(["d","b","c","b","c","a"], 2))
print(solution.kthDistinct(["aaa","aa","a"], 1))
print(solution.kthDistinct(["a","b","a"], 3))