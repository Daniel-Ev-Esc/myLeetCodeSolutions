class Solution(object):
    def maximumGain(self, s, x, y):
        """
        :type s: str
        :type x: int
        :type y: int
        :rtype: int
        """
        def getSubPoints(s,sub,points):
            stack = []
            total = 0
            for char in s:
                if stack and stack[-1] == sub[0] and char == sub[1]:
                    stack.pop()
                    total += points
                else:
                    stack.append(char)
            remaining = ''.join(stack)
            return remaining, total


        
        if x > y:
            newString, points = getSubPoints(s,"ab",x)
            newString, ad_points = getSubPoints(newString,"ba",y)
            points += ad_points
        else:
            newString, points = getSubPoints(s,"ba",y)
            newString, ad_points = getSubPoints(newString,"ab",x)
            points += ad_points
            
        return points

        
solution = Solution()

solution.maximumGain("cdbcbbaaabab",4,5)
solution.maximumGain("aabbaaxybbaabb",5,4)

"cdbcbbaaabab"
"cdbcbaab"
"cdbcab"

