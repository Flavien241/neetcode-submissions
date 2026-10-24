class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res=[]
        if (len(strs) == 0):
            return res
        dico = {}      
        for i in range(0,len(strs)):
            if not("".join(sorted(strs[i])) in dico.keys()):
                dico["".join(sorted(strs[i]))] = [strs[i]]
            else:
                dico["".join(sorted(strs[i]))].append(strs[i])
        return list(dico.values())


    def isInres(self, dico, mot):
        for valeur in dico.values():
                if (mot in valeur):
                    return True
        return False

    def isAnagram(self, s, t):
        dico1 = {}
        dico2 = {}
        if (len(s) != len(t)):
            return False
        for i in range(len(s)):
            if (s[i] in dico1):
                dico1[s[i]] += 1
            else:
                dico1[s[i]] = 0
            if (t[i] in dico2):
                dico2[t[i]] += 1
            else:
                dico2[t[i]] = 0
        if (dico1 == dico2):
            return True
        return False



        