# 136. Single Number

import collections
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # using xor to solve the problem
        # if two number have same bit, xor will become 0, therefor we can find the one left in a list
        res = 0
        for num in nums:
            res = num ^ res
        
        return res

    def singleNumber_hash(self, nums: List[int]) -> int:
        hash_table = defaultdict(int)
        for i in nums:
            hash_table[i] += 1
        
        for i in hash_table:
            if hash_table[i] == 1:
                return i
