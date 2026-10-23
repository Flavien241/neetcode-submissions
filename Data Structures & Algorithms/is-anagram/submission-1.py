class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dico1 = {}
        dico2 = {}
        if len(s) != len(t):
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
        if (dico1 != dico2):
            return False
        return True



