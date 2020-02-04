class Solution:
    """
    @param m: An integer m denotes the size of a backpack
    @param A: Given n items with size A[i]
    @return: The maximum size
    """

    def backPack(self, m, A):
        # write your code here
        n = len(A)
        dp = [[0] * (m + 1) for _ in range(n + 1)]
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                dp[i][j] = dp[i - 1][j]
                if j >= A[i - 1]:
                    dp[i][j] = max(dp[i][j], dp[i - 1][j - A[i - 1]] + A[i - 1])

        return dp[-1][-1]

    def backPack2(self, m, A):
        # write your code here
        dp = [0] * (m + 1)
        for v in A:
            for j in range(m, v - 1, -1):
                dp[j] = max(dp[j], dp[j - v] + v)

        return dp[-1]
