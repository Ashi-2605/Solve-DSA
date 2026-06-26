from bisect import bisect_left

class Solution:
    def countMajoritySubarrays(self, nums, target):
        n = len(nums)

        prefix = [0]
        s = 0
        for x in nums:
            if x == target:
                s += 1
            else:
                s -= 1
            prefix.append(s)

        values = sorted(set(prefix))
        size = len(values)

        bit = [0] * (size + 1)

        def update(i):
            while i <= size:
                bit[i] += 1
                i += i & -i

        def query(i):
            res = 0
            while i > 0:
                res += bit[i]
                i -= i & -i
            return res

        ans = 0

        for p in prefix:
            idx = bisect_left(values, p) + 1
            ans += query(idx - 1)
            update(idx)

        return ans