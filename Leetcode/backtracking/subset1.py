class Solution(object):
    def subsets(self, nums):
        nums_subsets = []
        self.iterate_nums([], nums_subsets, nums)
        return nums_subsets
    def iterate_nums(self, tags, num_subsets, nums):
        if len(tags)>len(nums):
            return 
        elif len(tags)==len(nums):
            subset_arr = []
            for i in range(len(tags)):
                if tags[i]:
                    subset_arr.append(nums[i])
            num_subsets.append(subset_arr)
           
        else:
            self.iterate_nums(tags+[0], num_subsets, nums)
            self.iterate_nums(tags+[1], num_subsets, nums)
            
s=Solution()
res = s.subsets(nums=[5,1,6])
print(res)