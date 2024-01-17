def get_min_and_max(arr):
    n_min = min(arr)
    n_max = max(arr)

    return [n_min, n_max]

arr1 = [2, 4, 1, 0, 2, -1]
arr2 = [20, 50, 12, 6, 14, 8]
arr3 = [100, -100]

print(get_min_and_max(arr1))
print(get_min_and_max(arr2))
print(get_min_and_max(arr3))

