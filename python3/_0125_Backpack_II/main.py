class Solution:
    """
    @param m: An integer m denotes the size of a backpack
    @param A: Given n items with size A[i]
    @param V: Given n items with value V[i]
    @return: The maximum value
    """

    def backPackII(self, m, A, V):
        # write your code here
        n = len(A)
        dp = [[0] * (m + 1) for _ in range(n + 1)]
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                dp[i][j] = dp[i - 1][j]
                if j >= A[i - 1]:
                    dp[i][j] = max(dp[i][j], dp[i - 1][j - A[i - 1]] + V[i - 1])

        return dp[-1][-1]

    def backPackII2(self, m, A, V):
        # write your code here
        n = len(A)
        dp = [0] * (m + 1)
        for i in range(1, n + 1):
            for j in range(m, A[i - 1] - 1, -1):
                dp[j] = max(dp[j], dp[j - A[i - 1]] + V[i - 1])

        return dp[-1]
