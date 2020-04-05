# 不同路径2

class Solution(object):
    def uniquePathsWithObstacles(self,obstacleGrid):
        # 定义状态：即数据元素的含义：dp表示当前位置的路径条数
        # 建立状态转移方程：dp[i] = dp[i]+dp[i-1]
        # 设定初始值：及优化数组空间，将二维数组压缩到一维数组，逐行计算当前最新路径条数，并覆盖上一行
        # 选区dp[-2]表示到达finish位置的路径总条数

        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        dp = [1] + [0]*n
        for i in range(m):
            for j in range(n):
                dp[j] = 0 if obstacleGrid[i][j] else dp[j]+dp[j-1]
            
        return dp[-2]
