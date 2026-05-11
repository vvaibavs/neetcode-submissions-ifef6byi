class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join(char for char in s if char.isalnum())
        s = s.lower()
        beginning = 0
        end = len(s) - 1
        print(s)

        while beginning <= end:
            if(s[beginning] != s[end]):
                return False
            
            beginning += 1
            end -= 1
        
        return True