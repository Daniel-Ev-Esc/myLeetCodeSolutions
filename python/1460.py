class Solution(object):
    def canBeEqual(self, target, arr):
        """
        :type target: List[int]
        :type arr: List[int]
        :rtype: bool
        """
        def mergesort(arr):
                
                if len(arr) == 1:
                     return arr
                arr1 = []
                arr2 = []
                for i in range(0, len(arr)):
                    if i < len(arr)//2:
                        arr1.append(arr[i])
                    else:
                        arr2.append(arr[i])
                
                arr1 = mergesort(arr1)
                arr2 = mergesort(arr2)

                return merge(arr1, arr2)
        
        def merge(arr1, arr2):

            arr3 = []

            i = 0
            j = 0

            while(i < len(arr1) and j < len(arr2)):
                if(arr1[i] < arr2[j]):
                    arr3.append(arr1[i])
                    i+=1
                else:
                    arr3.append(arr2[j])
                    j+=1
            
            while(i < len(arr1)):
                arr3.append(arr1[i])
                i+=1

            while(j < len(arr2)):
                arr3.append(arr2[j])
                j+=1
            
            return arr3

        return mergesort(target) == mergesort(arr)
        

solution = Solution()

print(solution.canBeEqual([1,2,3,4],[2,4,1,3]))
print(solution.canBeEqual([7],[7]))
print(solution.canBeEqual([3,7,9],[3,7,11]))


