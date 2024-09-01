class Solution(object):
    def sortArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
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
        
        return mergesort(nums)

solution = Solution()

print(solution.sortArray([5,2,3,1]))
print(solution.sortArray([5,1,1,2,0,0]))