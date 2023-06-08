def wildcard_matching(s, p) -> bool:
    n, m = len(s), len(p)
    dp = [[False] * (m + 1) for _ in range(n + 1)]
    dp[0][0] = True
    for j in range(1, m + 1):
        if p[j - 1] == '*':
            dp[0][j] = dp[0][j - 1]
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if p[j - 1] == s[i - 1] or p[j - 1] == '?':
                dp[i][j] = dp[i - 1][j - 1]
            elif p[j - 1] == '*':
                dp[i][j] = dp[i - 1][j] or dp[i][j - 1]
            else:
                dp[i][j] = False
    return dp[n][m]


assert wildcard_matching('aa', 'a') == False
assert wildcard_matching('aa', '*') == True
assert wildcard_matching('cb', '?a') == False
assert wildcard_matching('adceb', '*a*b') == True
assert wildcard_matching('acdcb', 'a*c?b') == False
