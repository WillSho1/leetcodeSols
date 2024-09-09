class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for char in s:
            if char in '({[':
                stack.append(char)
            if char in ')}]':
                opposite = '(' if char == ')' else ('{' if char == '}' else '[')
                if len(stack) == 0 or opposite != stack.pop():
                    return False
        return len(stack) == 0
            