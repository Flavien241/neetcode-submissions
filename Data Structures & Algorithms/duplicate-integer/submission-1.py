class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        if (len(nums) == 0):
            return False
        tab = []
        tab.append(nums[0])
        for i in range(1,len(nums)):
            if (nums[i] in tab):
                return True
            tab.append(nums[i])
        return False
        