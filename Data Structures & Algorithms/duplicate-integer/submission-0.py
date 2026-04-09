class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hshmp = {}

        for i in nums:
            if hshmp.get(i):
                return True
            else:
                hshmp[i] = 1
                continue
        return False
        