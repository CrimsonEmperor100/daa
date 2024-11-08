def knapsack(weights, values, capacity):
    n = len(values)
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(1, capacity + 1):
            if weights[i - 1] <= w:
                dp[i][w] = max(values[i - 1] + dp[i - 1][w - weights[i - 1]], dp[i - 1][w])
            else:
                dp[i][w] = dp[i - 1][w]

    return dp[n][capacity]


# User-friendly input
try:
    n = int(input("Enter the number of items: "))
    weights = list(map(int, input(f"Enter the weights of {n} items (separated by spaces): ").split()))
    values = list(map(int, input(f"Enter the values of {n} items (separated by spaces): ").split()))
    capacity = int(input("Enter the capacity of the knapsack: "))

    if len(weights) != n or len(values) != n:
        print("The number of weights and values must match the number of items!")
    elif capacity < 0:
        print("Knapsack capacity must be a positive number!")
    else:
        max_value = knapsack(weights, values, capacity)
        print(f"\nMaximum value in the knapsack: {max_value}")
except ValueError:
    print("Invalid input! Please ensure all inputs are numeric.")
