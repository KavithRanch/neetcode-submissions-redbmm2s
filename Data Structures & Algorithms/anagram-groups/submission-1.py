class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hshmp = {}
        for i, string in enumerate(strs):
            srt = "".join(sorted(string))
            if srt in hshmp:
                hshmp[srt].append(i)
            else:
                hshmp[srt] = [i]
        res = []
        for key in hshmp:
            temparr = []
            for i in hshmp[key]:
                temparr.append(strs[i])
            res.append(temparr)
        return res