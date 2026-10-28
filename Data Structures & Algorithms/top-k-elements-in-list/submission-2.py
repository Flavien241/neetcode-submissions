class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dico = {}
        for i in range(0,len(nums)):
            if not(nums[i] in dico.keys()):
                dico[nums[i]] = 0
            else:
                dico[nums[i]] += 1
        resultat = dict(sorted(dico.items(), key=lambda x: x[1], reverse=True))
        # Trier un dictionnaire par ordre décroissant de ses valeurs.
#
# 1. dico.items() :
#    Récupère les couples (clé, valeur) du dictionnaire.
#    Exemple : ("k", 8), ("h", 4), ("y", 12)
#
# 2. sorted() :
#    Trie les éléments et retourne une liste.
#
# 3. key=lambda x: x[1] :
#    Indique à sorted() de trier selon les valeurs.
#    x représente un couple (clé, valeur).
#    x[0] = clé ; x[1] = valeur.
#
# 4. reverse=True :
#    Trie par ordre décroissant (du plus grand au plus petit).
#
# 5. dict() :
#    Convertit la liste de couples triés en dictionnaire.
        return list(resultat.keys())[:k]

        
        