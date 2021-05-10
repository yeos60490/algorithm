class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        while val in nums:
            del nums[nums.index(val)]
