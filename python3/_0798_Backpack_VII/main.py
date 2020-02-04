"""
Assume that you have n yuan. There are many kinds of rice in the supermarket.
Each kind of rice is bagged and must be purchased in the whole bag.
Given the weight, price and quantity of each type of rice, find the maximum weight of rice that you can purchase.

"""


class Solution:
    """
    @param n: the money of you
    @param prices: the price of rice[i]
    @param weight: the weight of rice[i]
    @param amounts: the amount of rice[i]
    @return: the maximum weight
    """

    def backPackVII(self, n, prices, weight, amounts):
        m = len(prices)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                dp[i][j] = max(dp[i][j], dp[i - 1][j])
                k = 1
                while k <= amounts[i - 1] and j >= k * prices[i - 1]:
                    dp[i][j] = max(dp[i][j], dp[i - 1][j - k * prices[i - 1]] + k * weight[i - 1])
                    k += 1

        return dp[-1][-1]
