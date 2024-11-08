class Node:
    def __init__(self, level, profit, weight, bound):
        self.level = level
        self.profit = profit
        self.weight = weight
        self.bound = bound

def bound(u, n, capacity, weights, values):
    if u.weight >= capacity:
        return 0
    profit_bound = u.profit
    j = u.level + 1
    total_weight = u.weight
    while j < n and total_weight + weights[j] <= capacity:
        total_weight += weights[j]
        profit_bound += values[j]
        j += 1
    if j < n:
        profit_bound += (capacity - total_weight) * values[j] / weights[j]
    return profit_bound

def knapsack(capacity, weights, values, n):
    queue = []
    u = Node(-1, 0, 0, 0)
    v = Node(-1, 0, 0, 0)
    max_profit = 0
    u.bound = bound(u, n, capacity, weights, values)
    queue.append(u)
    while queue:
        u = queue.pop(0)
        if u.level == -1:
            v.level = 0
        if u.level == n - 1:
            continue
        v.level = u.level + 1
        v.weight = u.weight + weights[v.level]
        v.profit = u.profit + values[v.level]
        if v.weight <= capacity and v.profit > max_profit:
            max_profit = v.profit
        v.bound = bound(v, n, capacity, weights, values)
        if v.bound > max_profit:
            queue.append(Node(v.level, v.profit, v.weight, v.bound))
        v.weight = u.weight
        v.profit = u.profit
        v.bound = bound(v, n, capacity, weights, values)
        if v.bound > max_profit:
            queue.append(Node(v.level, v.profit, v.weight, v.bound))
    return max_profit

def user_input():
    n = int(input("Enter the number of items: "))
    weights = []
    values = []
    print("Enter the weights of the items:")
    for i in range(n):
        weight = int(input(f"Weight of item {i + 1}: "))
        weights.append(weight)

    print("Enter the values of the items:")
    for i in range(n):
        value = int(input(f"Value of item {i + 1}: "))
        values.append(value)
    capacity = int(input("Enter the capacity of the knapsack: "))

    return capacity, weights, values, n

if __name__ == "__main__":
    capacity, weights, values, n = user_input()
    max_profit = knapsack(capacity, weights, values, n)
    
    print(f"\nMaximum profit that can be obtained: {max_profit}")
    
    
    
    
