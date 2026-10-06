class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        dp = [[1]]
        for i in range(1, numRows):
            row = [1]
            for j in range(1, len(dp[i-1])):
                row.append(dp[i-1][j-1] + dp[i-1][j])
            row.append(1)
            dp.append(row)
        return dp