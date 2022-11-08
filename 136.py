# 136. Single Number

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # using xor to solve the problem
        # if two number have same bit, xor will become 0, therefor we can find the one left in a list
        res = 0
        for num in nums:
            res = num ^ res
        
        return res