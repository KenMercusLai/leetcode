class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in list(set(nums)):
            try:
                a, b = nums.index(i), nums.index(target - i)
                if a == b:
                    return a, nums[a + 1:].index(target - i) + a + 1
                else:
                    return a, b
            except ValueError:
                pass
