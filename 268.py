# 268. Missing Number

class Solution:
    def missingNumber_sum(self, nums: List[int]) -> int:
        res = 0
        for i in range(len(nums)+1):
            res += i
        
        for i in range(len(nums)):
            res -= nums[i]

        return res

    def missingNumber_bit(self, nums: List[int]) -> int:
        res = 0
        for i in range(len(nums)+1):
            res = i ^ res
        
        for i in range(len(nums)):
            res = res ^ nums[i]

        return res