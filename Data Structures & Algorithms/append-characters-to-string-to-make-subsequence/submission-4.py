class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        i = 0
        count = 0
        for i in range(len(s)):
            if count == len(t):
                break
            if s[i] == t[count]:
                count+=1
        return len(t) - count