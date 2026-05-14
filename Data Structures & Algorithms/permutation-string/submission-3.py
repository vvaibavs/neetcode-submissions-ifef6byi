class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        freq = [0] * 26
        for s in s1:
            freq[ord(s) - ord('a')] += 1
        
        for i in range(len(s2) - len(s1) + 1):
            tempfreq = [0] * 26
            for j in range(i, i + len(s1)):
                tempfreq[ord(s2[j]) - ord('a')] += 1
            if tempfreq == freq:
                return True
        return False
        