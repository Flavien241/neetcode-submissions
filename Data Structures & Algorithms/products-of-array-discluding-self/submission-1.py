class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        gauche = [1] * len(nums)
        droite = 1
        res = [1] * len(nums)
        for i in range(1,len(nums)):
            gauche[i] = gauche[i-1]*nums[i-1]

        for i in range(len(nums)-1, -1, -1):
            res[i] = gauche[i]*droite
            droite *= nums[i]

        return res