def merge(left, right):
    if not left: # When the length of the array is one
        return right
    
    if not right:
        return left

    if left[0] <= right[0]:
        return [left[0]] + merge(left[1:], right) #keep the smallest value and rerun the process on the rest

    return [right[0]] + merge(left, right[1:])


def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2

    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)