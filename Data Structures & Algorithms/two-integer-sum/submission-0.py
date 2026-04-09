class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hshmp = {}
        hshmp[nums[0]] = 0

        for i, num in enumerate(nums[1:]):
            diff = target - num
            print(hshmp, diff)
            if diff in hshmp:
                return [hshmp[diff], i + 1]
            else:
                hshmp[num] = i + 1