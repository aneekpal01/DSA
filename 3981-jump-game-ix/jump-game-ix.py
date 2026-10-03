class Solution(object):
    def maxValue(self, nums):
        n = len(nums)

        # Prefix maximum
        pre_max = [nums[0]] * n

        for i in range(1, n):
            pre_max[i] = max(pre_max[i - 1], nums[i])

        # Calculate answer from right to left
        ans = [0] * n
        suf_min = float('inf')

        for i in range(n - 1, -1, -1):

            if pre_max[i] > suf_min:
                ans[i] = ans[i + 1] if i + 1 < n else pre_max[i]
            else:
                ans[i] = pre_max[i]

            suf_min = min(suf_min, nums[i])

        return ans