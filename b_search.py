def binary_search(arr, key_value):
    start = 0
    end = len(arr) - 1

    while start <= end:
        mid = (start + end) // 2

        mid_value = arr[mid]

        if mid_value == key_value:
            return mid
        elif key_value < mid_value:
            end = mid - 1
        elif key_value > mid_value:
            start = mid + 1
    return -1

sorted_numbers = [11,22,33,44,55,66,77,88,99]
key = 77
#index_found =binary_search(key_value=key,arr=sorted_numbers)
index_found = binary_search(sorted_numbers, key)
print(f"BInary search for Target: {key} found at {index_found} ")

if index_found == -1:
    print(f"Binary search for Target:{key} found at {index_found} ")
elif index_found == -1:
    print(f"Item not found")

'''def recursive_binary_search(arr,target,start_index,end_index):
    if start_index > end_index:
        return -1
    mid = (start_index + end_index) // 2
    mid_value = arr[mid]
    if mid_value == target:
        return mid
    elif mid_value < target:
        return recursive_binary_search(arr,target,mid+1,start_index)
    else:
        return recursive_binary_search(arr,target,start_index,mid-1)
'''