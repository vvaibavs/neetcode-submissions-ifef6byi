class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closeToOpen = {")": "(", "]" : "[", "}" : "{"}

        for letter in s:
            if letter in closeToOpen:
                if stack and stack[-1] == closeToOpen[letter]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(letter)
        return len(stack) == 0