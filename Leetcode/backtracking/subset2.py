class Solution(object):
    '''
    The key is sort the array first
    Observe the order of generating the subset
    '''
    def subsets(self, nums):
        nums_subsets = []
        nums.sort()
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
            if subset_arr not in num_subsets:
              num_subsets.append(subset_arr)
           
        else:
            self.iterate_nums(tags+[0], num_subsets, nums)
            self.iterate_nums(tags+[1], num_subsets, nums)
            
s=Solution()
res = s.subsets(nums=[4,4,4,1,4])
print(res)

