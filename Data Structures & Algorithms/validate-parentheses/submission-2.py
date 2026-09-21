class Solution:
    def isValid(self, s: str) -> bool:
        stack = deque()
        d = {'(': ')', '[': ']', '{': '}'}
        for val in s:
            if val in d:
                stack.append(d[val])
            else:
                if not stack:
                    return False
                other = stack.pop()
                if other != val:
                    return False

        if stack:
            return False
        return True