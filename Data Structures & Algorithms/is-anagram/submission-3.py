class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_hash = {}
        for let in s:
            if let in s_hash:
                s_hash[let] += 1
            else:
                s_hash[let] = 1
        
        for let in t:
            if let in s_hash:
                if s_hash[let] == 0:
                    return False
                s_hash[let] -= 1
            else:
                return False
        
        for vals in s_hash.values():
            if vals != 0:
                return False
        return True