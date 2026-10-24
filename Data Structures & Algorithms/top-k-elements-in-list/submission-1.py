class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dico = {}
        for i in range(0,len(nums)):
            if not(nums[i] in dico.keys()):
                dico[nums[i]] = 0
            else:
                dico[nums[i]] += 1
        resultat = dict(sorted(dico.items(), key=lambda x: x[1], reverse=True))
        return list(resultat.keys())[:k]

        
        