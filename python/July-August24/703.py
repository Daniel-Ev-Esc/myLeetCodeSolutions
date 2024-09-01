class KthLargest(object):

    k = 0
    nums = []

    def __init__(self, k, nums):
        """
        :type k: int
        :type nums: List[int]
        """
        self.k = k
        self.nums = sorted(nums)

        

    def add(self, val):
        """
        :type val: int
        :rtype: int
        """
        i = 0

        while i < len(self.nums) and val > self.nums[i]:
            i += 1

        self.nums.insert(i, val)
        return self.nums[-self.k]

objects = KthLargest(3, [4, 5, 8, 2])

print(objects.add(3))
print(objects.add(5))
print(objects.add(10))
print(objects.add(9))
print(objects.add(4))

