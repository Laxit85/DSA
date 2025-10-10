# Valid Parenthesis

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        mapping = {')': '(', '}': '{', ']': '['}

        for ch in s:
            # If it's a closing bracket
            if ch in mapping:
                if stack and stack[-1] == mapping[ch]:
                    stack.pop()
                else:
                    return False
            else:
                # It's an opening bracket
                stack.append(ch)
        
        # If stack is empty → all brackets matched
        return not stack

# Example usage:
solution = Solution()
print(solution.isValid("()"))        # Output: True
print(solution.isValid("()[]{}"))    # Output: True
print(solution.isValid("(]"))        # Output: False
print(solution.isValid("([)]"))      # Output: False