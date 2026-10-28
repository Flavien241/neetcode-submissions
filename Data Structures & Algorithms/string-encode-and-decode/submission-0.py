class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for mot in strs:
            res += str(len(mot)) + "#" + mot
        print(res)
        return res



    def decode(self, s: str) -> List[str]:
        taille = 0
        res = []
        i=0
        indice_debut=0
        while i < len(s):
            if s[i] == "#":
                taille = int(s[indice_debut:i])
                res += [s[i+1:i+1+taille]]
                i+=taille
                indice_debut = i+1
            i+=1
        return res
        
            

