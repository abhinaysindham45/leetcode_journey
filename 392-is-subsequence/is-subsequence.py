class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        # strr = ""
        # for i in t:
        #     if i in s:
        #         strr += i
        #         print(strr)
        # if strr == s:
        #     return True
        # else:
        #     return False
        i = j = 0
        while i < len(s) and j < len(t):
            print(s[i],t[j])
            if s[i] == t[j]:
                i += 1
            j += 1
        return i == len(s)
        
