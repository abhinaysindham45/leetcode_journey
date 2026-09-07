class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        count = 0
        for i in nums:
            l = len(str(abs(i)))
            if l % 2 == 0:
                count += 1
        return count