def wordBreak(string, dictionary):
     
    # create a dp table to store results of subproblems
    # value of dp[i] will be true if string string can be segmented
    # into dictionary words from 0 to i.
    dp = [False for i in range(len(string) + 1)]
 
    # dp[0] is true because an empty string can always be segmented.
    dp[0] = True
 
    for i in range(len(string) + 1):
        for j in range(i):
            print(f"i:{i}, j:{j} = {string[j:i]}")
            if dp[j] and string[j:i] in dictionary:
                dp[i] = True
                break
     
    return dp[len(string)]

print(wordBreak("ilikeicecream", ["i", "like", "ice", "cream"]))