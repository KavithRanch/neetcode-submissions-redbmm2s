class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hsh = {}
        hsh[nums[0]] = 0
        for i, num in enumerate(nums[1:]):
            diff = target - num
            if diff in hsh:
                return [hsh[diff], i + 1]
            else:
                hsh[num] = i + 1
            print(hsh)