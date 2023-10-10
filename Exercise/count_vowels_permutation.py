def count_vowels_permutation(param_1):
    dp = [[0] * 5 for _ in range(param_1)]
    mod = 10**9 + 7

    # Base case: length 1 strings
    for i in range(5):
        dp[0][i] = 1

    for i in range(1, param_1):
        # Rules for 'a'
        dp[i][0] = (dp[i - 1][1] + dp[i - 1][2] + dp[i - 1][4]) % mod
        # Rules for 'e'
        dp[i][1] = (dp[i - 1][0] + dp[i - 1][2]) % mod
        # Rules for 'i'
        dp[i][2] = (dp[i - 1][1] + dp[i - 1][3]) % mod
        # Rules for 'o'
        dp[i][3] = dp[i - 1][2] % mod
        # Rules for 'u'
        dp[i][4] = (dp[i - 1][2] + dp[i - 1][3]) % mod

    return sum(dp[-1]) % mod