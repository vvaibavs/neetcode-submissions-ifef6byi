class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        second = 0
        temp = []
        maxLength = 0
        while second < len(s):
            print(ord(s[second]))
            if ord(s[second]) not in temp:
                temp.append(ord(s[second]))
                second+=1
            else:
                if len(temp) > maxLength:
                    maxLength = len(temp)
                second = second - len(temp) + 1
                temp = []
        if len(temp) > maxLength:
            maxLength = len(temp)
        return maxLength
        