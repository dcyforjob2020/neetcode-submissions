class Solution:
    # time complexity: O(n)
    # space complexity: O(n)
    def isValid(self, s: str) -> bool:
        # 
        parentheses_dict = {}
        parentheses_dict[")"] = "("
        parentheses_dict["]"] = "["
        parentheses_dict["}"] = "{"

        # stack
        stack = []

        # loop through s
        for c in s:
            # check if c is )
            # check if c is ]
            # check if c is }
            if c in parentheses_dict:
                # there is no open bracket
                if not stack:
                    return False

                # not the same type of bracket
                if stack.pop() != parentheses_dict[c]:
                    return False
            else:
                stack.append(c)

        # if stack not empty return False, else True
        return not stack