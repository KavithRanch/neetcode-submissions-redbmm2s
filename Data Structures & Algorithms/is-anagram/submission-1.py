class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hshmp = {}

        for i in s:
            if hshmp.get(i):
                hshmp[i] += 1
                continue
            hshmp[i] = 1
        
        for j in t:
            if hshmp.get(j):
                if hshmp[j] == 0:
                    return False
                hshmp[j] -= 1
            else:
                return False

        for val in hshmp.values():
            if val != 0:
                return False     
        return True
            