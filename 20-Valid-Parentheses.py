class Solution:
    def isValid(self, s: str) -> bool:
        bracket_dict ={')':'(', '}':'{',']':'['}
        stack=[]

        for char in s:
            if char in bracket_dict.values() :
                stack.append(char)
            elif char in bracket_dict :
                if stack and stack[-1] == bracket_dict[char]:
                    stack.pop()
                else:
                    return False
            else:
                return False

        return not stack
