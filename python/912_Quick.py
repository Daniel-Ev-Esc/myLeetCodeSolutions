class Solution(object):
    def sortArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        def quicksort(arr, ini, fin):

            if ini < fin:
                pivot_index = partition(arr, ini, fin)
                quicksort(arr, ini, pivot_index-1)
                quicksort(arr, pivot_index+1, fin)
            return arr
        
        def partition(arr, ini, fin):
            pivot = arr[fin]

            counter = 0
            lastSmallest = ini-1

            aux = 0

            for i in range(ini, fin):
                if arr[i] < pivot:
                    aux = arr[lastSmallest+1]
                    arr[lastSmallest+1] = arr[i]
                    arr[i] = aux
                    lastSmallest += 1
                counter +=1
            
            arr[lastSmallest + 1], arr[fin] = arr[fin], arr[lastSmallest + 1]
            return lastSmallest+1
            
        return quicksort(nums, 0, len(nums)-1)

solution = Solution()

print(solution.sortArray([5,2,3,1]))
print(solution.sortArray([5,1,1,2,0,0]))