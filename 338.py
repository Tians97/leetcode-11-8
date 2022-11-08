# 338. Counting Bits

class Solution:
    def countBits(self, n: int) -> List[int]:
        # create a empty arr
        res = []
        # iterate number from 0 to n
        for i in range(n+1):
            # using bin to change int to bit, and count for 1 in the bit, append number into the res
            res.append(bin(i).count("1"))

        return res
