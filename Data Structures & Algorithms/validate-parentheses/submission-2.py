class Solution:
    def isValid(self, s: str) -> bool:
# create hashmap of valid pairs
# check closed parens
# create stack to solve order effeciently
# open parens can be added
        paren_stack = []
        paren_map = {")":"(", "]": "[", "}": "{"}
# iterate through str once
# check if paren is is in paren_map
# if not, append to stack
# if yes, check if key matches val
# return false if not
# pop off top of stack if so
# return true once stack is empty
        for c in s:
            if c in paren_map:
                if paren_stack and paren_stack[-1] == paren_map[c]:
                    paren_stack.pop()
                else:
                    return False
            else:
                paren_stack.append(c)
        
        if not paren_stack:
            return True
        return False

# its important to remember why this works.
# open parens can be appended to stack as they dont have a closure requirement
# closed parens need to match
# the stack is empty means that all parens got matched
