class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # Solution 1 : approche personnelle
        # Complexité temporelle : O(n²)
        #
        # if len(nums) == 0:
        #     return False
        # tab = []
        # tab.append(nums[0])
        # for i in range(1, len(nums)):
        #     if nums[i] in tab:
        #         return True
        #     tab.append(nums[i])
        # return False

        # Solution 2 : optimisée avec set
        # Complexité temporelle : O(n) en moyenne
        return len(set(nums)) != len(nums)