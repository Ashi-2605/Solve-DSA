class Solution(object):
    def combinationSum(self, candidates, target):
        res = []

        def backtrack(start, target, path):
            if target == 0:
                res.append(path[:])
                return

            if target < 0:
                return

            for i in range(start, len(candidates)):
                path.append(candidates[i])

                # Use the same index again because we can reuse the same number
                backtrack(i, target - candidates[i], path)

                path.pop()  # Backtrack

        backtrack(0, target, [])
        return res
        