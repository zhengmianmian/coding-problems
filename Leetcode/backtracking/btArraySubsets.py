class Solution(object):
    def subsetXORSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        a tree, [0,1,1,0,1] whether contain an element
        till the leaf, cal the value
        """
        current_value = 0
        return self.iterate_nums([], current_value, nums)
    def iterate_nums(self, tags, current_value,nums):
        if len(tags)>len(nums):
            return 0
        elif len(tags)==len(nums):
            res = 0
            for i in range(len(tags)):
                if tags[i]:
                    res = res ^ nums[i]
            return current_value + res
        else:
            return self.iterate_nums(tags+[1],current_value,nums) + self.iterate_nums(tags+[0],current_value,nums)
            


s=Solution()
res = s.subsetXORSum(nums=[5,1,6])
print(res)