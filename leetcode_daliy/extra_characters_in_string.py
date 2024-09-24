s = "leetscode"
dictionary = ["leet","code","leetcode"]

n = len(s)
# dp[i] represents the minimum number of extra characters in s[0:i]
dp = [float('inf')] * (n + 1)
dp[0] = 0  # Base case: no extra characters for an empty string

# Convert the dictionary to a set for faster lookup
word_set = set(dictionary)

for i in range(1, n + 1):
    # Assume the current character (s[i-1]) is an extra character
    dp[i] = dp[i - 1] + 1

    # Check if there are any words that match a substring ending at index i
    for j in range(i):
        if s[j:i] in word_set:
            dp[i] = min(dp[i], dp[j])
print(dp[n])