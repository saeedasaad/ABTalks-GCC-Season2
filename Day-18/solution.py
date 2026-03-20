def isValid(s: str) -> bool:

    bracket_map = {')': '(', '}': '{', ']': '['}
    stack = [] 

    for char in s:
        if char in bracket_map.values():  
            stack.append(char)
        elif char in bracket_map:  
            if stack and stack[-1] == bracket_map[char]:
                stack.pop()  
            else:
                return False  
        else:
            return False 

    return not stack 

if __name__ == "__main__":
    test_cases = ["()", "()[]{}", "(]", "([)]", "{[]}"]
    for case in test_cases:
        print(f"{case}: {isValid(case)}")