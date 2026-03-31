class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            match c:
                case '(':
                    stack.append('(')
                case ')':
                    if stack == []:
                        return False
                    if stack[-1] == '(':
                        stack.pop(-1)
                    else:
                        return False
                case '[':
                    stack.append('[')
                case ']':
                    if stack == []:
                        return False
                    if stack[-1] == '[':
                        stack.pop(-1)
                    else:
                        return False
                case '{':
                    stack.append('{')
                case '}':
                    if stack == []:
                        return False
                    if stack[-1] == '{':
                        stack.pop(-1)
                    else:
                        return False
        return len(stack) == 0
