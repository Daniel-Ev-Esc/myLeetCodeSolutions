class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        countArr = []

        for element in nums:
            while len(countArr) < element+1:
                countArr.append(0)
            
            countArr[element] += 1
        
        print(countArr)
        j = 0

        for i in range(0, len(nums)):
            while countArr[j] == 0:
                j += 1
            
            countArr[j] -= 1
            nums[i] = j

        print(nums)

solution = Solution()

solution.sortColors([2,0,2,1,1,0])
