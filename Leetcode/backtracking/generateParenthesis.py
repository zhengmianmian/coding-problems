class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        str_len = n * 2
        parenthesis = []
        parenthesis_str = ""
        self.constructParenthesis(0, parenthesis_str, parenthesis, str_len)
        return parenthesis
        
    def constructParenthesis(self, current_index, parenthesis_str, parenthesis, str_len):
        if current_index >= str_len:
            if self.isParenthesisValid(parenthesis_str):
              parenthesis.append(parenthesis_str)
            return
        else:
            if parenthesis_str.count('(') > str_len/2 or parenthesis_str.count(')') > str_len/2:
                return
            else:
                self.constructParenthesis(current_index+1, parenthesis_str+'(', parenthesis, str_len)
                self.constructParenthesis(current_index+1, parenthesis_str+')', parenthesis, str_len)

    def isParenthesisValid(self, parenthesis):
        stack = []
        stack.append(parenthesis[0])
        i = 1
        while i < len(parenthesis):
            p = parenthesis[i]
            if len(stack) and stack[len(stack)-1] == '(' and p == ')':
                stack.pop()
            else:
                stack.append(p)
            i = i+1
        if len(stack):
            return False
        else:
            return True
    

s = Solution()
print(s.generateParenthesis(3))
        