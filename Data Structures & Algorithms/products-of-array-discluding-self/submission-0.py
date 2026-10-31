class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        gauche = [1] * len(nums)
        droite = [1] * len(nums)
        res = []
        for i in range(1,len(nums)):
            gauche[i] = gauche[i-1]*nums[i-1]

        for i in range(len(nums)-2, -1, -1):
            droite[i] = droite[i+1] * nums[i+1]

        for i in range(len(nums)):
            res.append(gauche[i] * droite[i])
        return res