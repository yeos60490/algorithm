class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        
        i = 0
        while i+1 < len(nums):
            if nums[i] == nums[i+1]:
                del nums[i+1]
            else:
                i += 1
                
