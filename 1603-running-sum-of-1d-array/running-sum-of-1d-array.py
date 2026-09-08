class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        sum = 0
        sum_a = []
        for i in range(len(nums)):
            sum += nums[i]
            sum_a.append(sum)
        return sum_a