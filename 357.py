class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        res = 0
        seen = set()

        def backtrack(num):
            nonlocal res
            if len(num) > n:
                return

            curr = int("".join(num)) if num else None
            if len(set(num)) == len(num) and curr and curr not in seen:
                seen.add(curr)
                res += 1
            
            for nm in ["0","1","2","3","4","5","6","7","8","9"]:
                num.append(nm)
                backtrack(num)
                num.pop()
            
        backtrack([])
        return res+1
