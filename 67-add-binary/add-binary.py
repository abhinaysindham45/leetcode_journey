class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a,b = int(a,2), int(b,2)
        c = a + b
        z = str(bin(c)[2:])
        return z
        