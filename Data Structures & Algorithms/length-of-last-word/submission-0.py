class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        arr = s.split(" ")
        noSpaces = []
        for a in arr:
            if a:
                noSpaces.append(a)
        return (len(noSpaces[len(noSpaces)-1]))