def lcs(str1, str2):
    dp = [[-1 for _ in range(len(str2)+1)] for _ in range(len(str1)+1)]
    return _lcs(str1, str2, len(str1), len(str2), dp)


def _lcs(str1, str2, len1, len2, dp):
    if len1 == 0 or len2 == 0:
        return 0

    if dp[len1][len2] != -1:
        return dp[len1][len2]

    # check last letter in each of the strings
    if str1[len1 - 1] == str2[len2 - 1]:
        dp[len1][len2] = 1 + _lcs(str1, str2, len1-1, len2-1, dp)
    else:
        dp[len1][len2] = max(_lcs(str1, str2, len1-1, len2, dp),
                             _lcs(str1, str2, len1, len2-1, dp))

    return dp[len1][len2]


X = "AGGTAB"
Y = "GXTXAYB"
print(f"LCS Length: {lcs(X,Y)}")
