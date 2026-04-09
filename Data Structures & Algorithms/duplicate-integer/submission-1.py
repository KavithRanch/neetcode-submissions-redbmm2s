class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hshmp = set()

        for i in nums:
            if i in hshmp:
                return True
            hshmp.add(i)
        return False
        