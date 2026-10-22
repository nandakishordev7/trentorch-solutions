def count_comparisions_linear_search(arr, target):
    comparisons = 0
    for value in arr:
        comparisons += 1
        if value == target:
            return True, comparisons
    return False, comparisons


def count_comparisions_binary_search(sorted_arr, target):
    lo, hi = 0, len(sorted_arr) - 1
    comparisions = 0
    while lo <= hi:
        mid = (lo + hi) // 2 
        comparisions += 1
        if sorted_arr[mid] == target:
            return True, comparisions
        elif sorted_arr[mid] < target:
            lo = mid + 1 
        else:
            hi = mid - 1
    return False, comparisions
