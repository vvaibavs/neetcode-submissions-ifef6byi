class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join(char for char in s if char.isalnum())
        s = s.lower()
        first = 0
        last = len(s)-1

        while last > first:
            if s[first] != s[last]:
                return False
            
            first+=1
            last-=1
        
        return True