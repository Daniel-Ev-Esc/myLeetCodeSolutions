class Solution(object):


    def reverseParentheses(self, s):
        """
        :type s: str
        :rtype: str
        """
        def reverseString(s):
            stack = []
            for char in s:
                stack.append(char)
            
            stringFinal = ""
            for char in s:
                stringFinal+= stack.pop()
            
            return stringFinal
        
        def reversePar(pos,s):
            stringToReverse = ""
            while pos < len(s) and s[pos] != ")":
                if s[pos] != "(":
                    stringToReverse += s[pos]
                    #print(stringToReverse)
                else:
                    #print("sub found")
                    pos, resultingString = reversePar(pos+1, s)
                    stringToReverse += resultingString
                    #print("Reversing:", stringToReverse)

                pos += 1

            return pos, reverseString(stringToReverse)
        
        def reverseParInit(pos,s):
            stringToReverse = ""
            while pos < len(s) and s[pos] != ")":
                if s[pos] != "(":
                    stringToReverse += s[pos]
                    #print(stringToReverse)
                else:
                    #print("sub found")
                    pos, resultingString = reversePar(pos+1, s)
                    stringToReverse += resultingString
                    #print("Reversing:", stringToReverse)

                pos += 1

            return stringToReverse
                
        finalString = reverseParInit(0,s)

        print(finalString)


        return finalString


solution = Solution()

solution.reverseParentheses("(abcd)")
solution.reverseParentheses("(u(love)i)")
solution.reverseParentheses("(ed(et(oc))el)")