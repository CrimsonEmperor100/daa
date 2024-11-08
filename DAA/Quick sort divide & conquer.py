def partition(arr, low, high):
    pivot = arr[high]  # Choosing the last element as the pivot
    i = low - 1  # Pointer for the smaller element

    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]  # Swap elements

    # Place the pivot in the correct position
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


def quick_sort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)  # Partition index
        quick_sort(arr, low, pi - 1)  # Recursively sort the left subarray
        quick_sort(arr, pi + 1, high)  # Recursively sort the right subarray


# User-friendly input
try:
    arr = list(map(int, input("Enter an array of numbers (separated by spaces): ").split()))
    quick_sort(arr, 0, len(arr) - 1)
    print("Sorted array:", arr)
except ValueError:
    print("Invalid input! Please enter numbers only.")
