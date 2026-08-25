class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # l = len(digits) - 1
        # digits[l] = digits[l] + 1
        # if digits[l] > 9:
        #     digits[l] = divmod(digits[l],10)
        # return digits
        for i in range(len(digits) - 1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits
            digits[i] = 0
        return [1] + digits
            
        