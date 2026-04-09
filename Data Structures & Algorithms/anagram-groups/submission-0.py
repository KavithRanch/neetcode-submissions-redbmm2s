class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hshmp = {}
            
        for i in strs:
            letter_map = [0] * 26
            for j in i:
                letter_map[ord(j)-97] += 1
            
            if tuple(letter_map) in hshmp:
                hshmp[tuple(letter_map)].append(i)
            else:
                hshmp[tuple(letter_map)] = [i]
        return list(hshmp.values())