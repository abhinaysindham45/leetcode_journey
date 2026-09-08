class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        tsum = sum(nums)
        lsum = 0

        for i, num in enumerate(nums):
            if lsum == (tsum - lsum - num):
                return i
            lsum += num
        return -1

        