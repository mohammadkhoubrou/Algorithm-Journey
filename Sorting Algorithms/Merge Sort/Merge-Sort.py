def merge(left, right):
    result = [] #the output
    i = 0  # left array pointer
    j = 0  # right array pointer

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    while i < len(left):		# add remaining elements when the pointer has reached the end of left array
        result.append(left[i])
        i += 1


    while j < len(right):		# add remaining elements when the pointer has reached the end of right array
        result.append(right[j])
        j += 1

    return result


def merge_sort(arr):
    if len(arr) <= 1: #base of recursion
        return arr

    mid = len(arr) // 2 #division
    left = arr[:mid]
    right = arr[mid:]


    left = merge_sort(left) 		#continue division on left and right side
    right = merge_sort(right)


    return merge(left, right) 	#merge

