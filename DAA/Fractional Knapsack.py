class Item:
    def __init__(self, value, weight):
        self.value = value
        self.weight = weight
        self.ratio = value / weight 

def fractional_knapsack(items, capacity):
    items.sort(key=lambda x: x.ratio, reverse=True)
    total_value = 0 

    for item in items:
        if capacity >= item.weight: 
            capacity -= item.weight
            total_value += item.value
        else:  
            total_value += item.ratio * capacity
            break

    return total_value

try:
    n = int(input("Enter the number of items: "))
    items = []
    
    for i in range(n):
        value = float(input(f"Enter value of item {i + 1}: "))
        weight = float(input(f"Enter weight of item {i + 1}: "))
        items.append(Item(value, weight))
    
    capacity = float(input("Enter the capacity of the knapsack: "))
    
    if capacity < 0:
        print("Knapsack capacity must be a positive number!")
    else:
        max_value = fractional_knapsack(items, capacity)
        print(f"\nMaximum value in the knapsack: {max_value:.2f}")
except ValueError:
    print("Invalid input! Please enter numeric values for weights, values, and capacity.")
