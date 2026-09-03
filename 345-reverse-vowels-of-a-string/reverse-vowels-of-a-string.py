class Solution:
    def reverseVowels(self, s):
        word = list(s)
        vow = "AEIOUaeiou"
        print(word)
        start,end = 0, len(s)-1
        while start < end:
            while start < end and vow.find(word[start]) == -1:
                start += 1
            while start < end and vow.find(word[end]) == -1:
                end -= 1
            word[start], word[end] = word[end], word[start]
            start += 1
            end -= 1
        return "".join(word)
        
                