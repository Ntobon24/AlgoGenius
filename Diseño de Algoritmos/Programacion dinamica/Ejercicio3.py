#Ejercicio 3
def min_difference(arr):
    n = len(arr)
    total_sum = sum(arr)

    dp = [[False for _ in range(total_sum+1)] for _ in range(n+1)]

    for i in range(n+1):
        dp[i][0] = True

    for i in range(1, n+1):
        for j in range(1, total_sum+1):
            dp[i][j] = dp[i-1][j]
            if arr[i-1] <= j:
                dp[i][j] |= dp[i-1][j-arr[i-1]]

    min_diff = float("inf")
    for j in range(total_sum // 2, -1, -1):
        if dp[n][j]:
            min_diff = total_sum - 2 * j
            break

    return min_diff

arr = [1, 4]
print(min_difference(arr))