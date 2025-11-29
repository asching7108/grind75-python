class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        results = []

        def backtrack(
            remain: int,
            start: int,
            comb: List[int]
        ) -> None:
            if remain == 0:
                results.append(list(comb))
                return

            if remain < 0:
                return

            for i in range(start, len(candidates)):
                candidate = candidates[i]
                comb.append(candidate)
                backtrack(remain - candidate, i, comb)
                comb.pop()

        backtrack(target, 0, [])

        return results