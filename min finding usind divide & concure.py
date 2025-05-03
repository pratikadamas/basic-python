


def find_min(arr, low, high):
    if low == high:
        return arr[low]
    mid = (low + high) // 2
    left_min = find_min(arr, low, mid)
    right_min = find_min(arr, mid + 1, high)
    return min(left_min, right_min)

# Example usage:
array = [5, 3, 8, 1, 9, 2]
minimum = find_min(array, 0, len(array) - 1)
print("Minimum element is:", minimum)