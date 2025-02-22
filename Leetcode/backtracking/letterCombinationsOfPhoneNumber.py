class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if len(digits) == 0:
            return []
        res_str_arr = []
        str_item = ""
        self.construct_str(0, str_item, digits, res_str_arr)
        return res_str_arr

    def construct_str(self, current_index, str_item, digits, res_str_arr):
        if current_index >= len(digits):
            res_str_arr.append(str_item)
            return
        else:
            letters_index = int(digits[current_index]) - 2
            for letter in self.LETTERS[letters_index]:
                self.construct_str(current_index+1, str_item+letter, digits,res_str_arr)

    LETTERS = [['a','b','c'],
               ['d','e','f'],
               ['g','h','i'],
               ['j','k','l'],
               ['m','n','o'],
               ['p','q','r','s'],
               ['t','u','v'],
               ['w','x','y','z']]

s = Solution()
res = s.letterCombinations("23")
print(res)