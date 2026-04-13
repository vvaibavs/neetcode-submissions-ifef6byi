class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sd = {}
        td = {}
        if len(s) != len(t):
            return False 
        for i in range(len(s)):
            if sd.get(s[i]) == None:
                sd[s[i]] = 1
            else:
                sd[s[i]] = sd.get(s[i]) + 1

        for i in range(len(t)):
            if td.get(t[i]) == None:
                td[t[i]] = 1
            else:
                td[t[i]] = td.get(t[i]) + 1

        return td == sd