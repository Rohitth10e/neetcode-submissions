class Solution:
    def countBits(self, n: int) -> List[int]:
        res = [0]
        for i in range(1, n+1):
            binary = bin(i)
            count = 0
            for bit in binary:
                if bit=="1":
                    count+=1
            res.append(count)
        return res