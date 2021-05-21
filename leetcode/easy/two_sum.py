class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            num1 = i
            diff = target - nums[i]
            if diff in nums[i+1:]:
                num2 = nums[i+1:].index(diff) + (i+1)
                return [num1, num2]
