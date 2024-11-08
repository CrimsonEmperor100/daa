def optimal_bst(keys, frequencies, n):
    cost = [[0 for x in range(n)] for y in range(n)]
    for i in range(n):
        cost[i][i] = frequencies[i]
    for length in range(2, n + 1): 
        for i in range(n - length + 1):
            j = i + length - 1
            cost[i][j] = float('inf') 
            freq_sum = sum(frequencies[i:j+1])
            for r in range(i, j + 1):
                left_cost = cost[i][r - 1] if r > i else 0
                right_cost = cost[r + 1][j] if r < j else 0
                total_cost = left_cost + right_cost + freq_sum
                cost[i][j] = min(cost[i][j], total_cost)

    return cost[0][n - 1]
try:
    n = int(input("Enter the number of keys: "))
    keys = []
    frequencies = []

    for i in range(n):
        key = int(input(f"Enter key {i + 1}: "))
        freq = int(input(f"Enter frequency of key {key}: "))
        keys.append(key)
        frequencies.append(freq)
    min_cost = optimal_bst(keys, frequencies, n)
    print(f"The minimum cost of the Optimal Binary Search Tree is: {min_cost}")

except ValueError:
    print("Please enter valid integer values for keys and frequencies.")
