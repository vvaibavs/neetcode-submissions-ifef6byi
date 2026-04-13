class Solution:
    def isPalindrome(self, s: str) -> bool:
        stri = ''.join(char for char in s if char.isalnum())
        strin = stri.lower()
        for i in range(0, (len(strin))):
            if (strin[i] != strin[len(strin) - i - 1]):
                return False
        return True