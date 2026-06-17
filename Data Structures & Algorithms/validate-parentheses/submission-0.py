class Solution:
    def isValid(self, s: str) -> bool:
        
        stack = []
        bracket_map = { ")" : "(", "]" : "[", "}" : "{" }

        for c in s:
            # if c is a CLOSING bracket
            if c in bracket_map:
                # when we see a closing bracket we check if the top of the stack has its match
                # and only if the stack is NOT empty
                if stack and stack[-1] == bracket_map[c]:
                    stack.pop()
                # if the check is false its not a valid string
                else:
                    return False
            # if its not a closing bracket it gets appended
            else:
                stack.append(c)
            
        # only return True if stack is empty because it could be something like "(((", all brackets must have a match
        return True if not stack else False