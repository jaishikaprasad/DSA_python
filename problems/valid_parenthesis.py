# Leetcode Ques:20 [valid_parethesis]
# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.

def valid_parethesis(s):
    stack = []
    for ch in s:
        if ch == ")":
            if len(stack) == 0 or stack.pop() != "(":
                return False
        elif ch == "}":
            if len(stack) == 0 or stack.pop() != "{":
                return False
        elif ch == "]":
            if len(stack) == 0 or stack.pop() != "[":
                return False   
        else:
            stack.append(ch)

    if len(stack) == 0:
        return True
    return False

print(valid_parethesis("(){}[]("))

# output : True