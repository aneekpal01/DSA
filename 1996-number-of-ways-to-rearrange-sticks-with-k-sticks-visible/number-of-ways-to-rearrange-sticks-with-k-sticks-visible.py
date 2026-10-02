class Solution(object):
    def rearrangeSticks(self, n, k):
        MOD = 10**9 + 7

        dp = [[0] * (k + 1) for _ in range(n + 1)]
        dp[0][0] = 1

        for i in range(1, n + 1):
            for j in range(1, min(i, k) + 1):
                # New tallest stick is visible
                visible = dp[i - 1][j - 1]

                # New tallest stick is NOT visible
                hidden = dp[i - 1][j] * (i - 1)

                dp[i][j] = (visible + hidden) % MOD

        return dp[n][k]
        