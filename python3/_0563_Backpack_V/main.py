class Solution:
    """
    @param nums: an integer array and all positive numbers
    @param target: An integer
    @return: An integer
    """

    def backPackV(self, nums, target):
        # write your code here
        n = len(nums)
        dp = [[0] * (target + 1) for _ in range(n + 1)]
        dp[0][0] = 1
        for i in range(1, n + 1):
            dp[i][0] = 1
            for j in range(1, target + 1):
                dp[i][j] = dp[i - 1][j]
                if j >= nums[i - 1]:
                    dp[i][j] += dp[i - 1][j - nums[i - 1]]

        return dp[-1][-1]

    def backPackV2(self, nums, target):
        # write your code here
        dp = [0] * (target + 1)
        dp[0] = 1
        for num in nums:
            for j in range(target, num - 1, -1):
                dp[j] += dp[j - num]

        return dp[-1]
