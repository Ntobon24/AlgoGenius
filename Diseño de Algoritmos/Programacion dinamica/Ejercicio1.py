# Paradigma utilizado -> Programación dinámica
def factorial(n):
    if n == 0 or n == 1:
        return 1
    dp = [0] * (n+1)
    dp[0] = 1
    dp[1] = 1

    for i in range(2, n+1):
        dp[i] = i * dp[i-1]
    return dp[n]
print(factorial(5)) 
