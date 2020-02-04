"""
Given n kind of items with size Ai and value Vi( each item has an infinite number available) and a backpack with size m.
What's the maximum value can you put into the backpack?

Example：
Given 4 items with size [2, 3, 5, 7] and value [1, 5, 2, 4], and a backpack with size 10. The maximum value is 15.
"""


class Solution:
    """
    @param m: An integer m denotes the size of a backpack
    @param A: Given n items with size A[i]
    @param V: Given n items with value V[i]
    @return: The maximum value
    """

    def backPackIII(self, m, A, V):
        # write your code here
        n = len(A)
        dp = [[0] * (m + 1) for _ in range(n + 1)]
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                dp[i][j] = dp[i - 1][j]
                if j >= A[i - 1]:
                    dp[i][j] = max(dp[i][j], dp[i][j - A[i - 1]] + V[i - 1])

        return dp[-1][-1]

    def backPackIII2(self, m, A, V):
        # write your code here
        n = len(A)
        dp = [0] * (m + 1)
        for i in range(1, n + 1):
            for j in range(A[i - 1], m + 1):
                dp[j] = max(dp[j], dp[j - A[i - 1]] + V[i - 1])

        return dp[-1]
