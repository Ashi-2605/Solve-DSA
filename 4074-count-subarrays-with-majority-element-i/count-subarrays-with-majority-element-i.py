class Solution:
    def countMajoritySubarrays(self, nums, target):
        n = len(nums)

        # Build prefix sums (+1 for target, -1 otherwise)
        prefix = [0]
        s = 0
        for x in nums:
            s += 1 if x == target else -1
            prefix.append(s)

        # Coordinate compression
        vals = sorted(set(prefix))
        rank = {v: i + 1 for i, v in enumerate(vals)}

        # Fenwick Tree
        m = len(vals)
        bit = [0] * (m + 1)

        def update(i):
            while i <= m:
                bit[i] += 1
                i += i & -i

        def query(i):
            res = 0
            while i > 0:
                res += bit[i]
                i -= i & -i
            return res

        ans = 0

        for x in prefix:
            idx = rank[x]
            ans += query(idx - 1)   # Count previous prefix sums < current
            update(idx)

        return ans


        