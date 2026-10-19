class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        
        #    e  z  u  p  k  r
        # u [0][0][1][1][1][1]
        # b [0][0][1][1][1][1]
        # m [0][0][1][1][1][1]
        # r [0][0][1][1][1][2]
        # a [0][0][1][1][1][2]
        # p [0][0][1][2][2][2]
        # g [0][0][1][2][2][2]
 
        #    j  m  j  k  b  k  j  k  v
        # b [0][0][0][0][1][1][1][1][1]
        # s [0][0][0][0][1][1][1][1][1]
        # b [0][0][0][0][1][1][1][1][1]
        # i [0][0][0][0][1][1][1][1][1]
        # n [0][0][0][0][1][1][1][1][1]
        # i [0][0][0][0][1][1][1][1][1]
        # n [0][0][0][0][1][1][1][1][1]
        # m [0][1][1][1][1][1][1][1][1]

        dp = [[0 for _ in range(len(text2)+1)] for _ in range (len(text1)+1)]

        for i in range(1, len(text1)+1):
            c1 = text1[i-1]
            for j in range(1, len(text2)+1):
                c2 = text2[j-1]
                if c1 == c2:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])

                
    
        return dp[-1][-1] 







