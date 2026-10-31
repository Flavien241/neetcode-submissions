class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = list(set(nums))
        nums.sort()
        maximum = 1
        tab = []
        if len(nums) == 0:
            return 0
        for i in range(1, len(nums)):
            if (nums[i]-nums[i-1] == 1):
                maximum+=1
                print(maximum)
            else:
                tab.append(maximum)
                maximum = 1
        tab.append(maximum)
        if len(tab)!=0:
            return max(tab)
        else:
            return maximum
            

        