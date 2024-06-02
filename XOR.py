from typing import List

class Solution:
    def constructList(self, q: int, queries: List[List[int]]) -> List[int]:
       
        ans = []
        x = 0
        
        for i in range(len(queries) - 1, -1, -1):
            if queries[i][0] == 0:
                ans.append(x ^ queries[i][1])
            else:
                x ^= queries[i][1]
        
        ans.append(0 ^ x)
        ans.sort()
        return ans
