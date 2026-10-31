class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        maximum = 1
        i = 0
        if len(nums) == 0:
            return 0
        for val in nums:
            if not (val-1 in nums):
                debut = val
                while debut+i in nums:
                    i+=1
                if i>=maximum:
                    maximum = i
                i=0
        return maximum
            
            

        