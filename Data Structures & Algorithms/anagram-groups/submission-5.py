class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if (len(strs) == 0):
            return []
        dico = {}      
        for i in range(0,len(strs)):
            if not("".join(sorted(strs[i])) in dico.keys()):
                dico["".join(sorted(strs[i]))] = [strs[i]]
            else:
                dico["".join(sorted(strs[i]))].append(strs[i])
        return list(dico.values())

        