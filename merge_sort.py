def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    # Perform merge_sort recursively on both halves
    left_half, right_half = merge_sort(arr[:mid]), merge_sort(arr[mid:])

    # Merge each side together
    return merge(left_half, right_half)

def merge(left, right):
    # Merging process
    left_pointer, right_pointer = 0, 0
    result = [] 
    while left_pointer < len(left) and right_pointer < len(right):
        if left[left_pointer] < right[right_pointer]:
            result.append(left[left_pointer])
            left_pointer += 1
        else:
            result.append(right[right_pointer])
            right_pointer += 1

    # Add the left overs if there's any
    result.extend(left[left_pointer:])
    result.extend(right[right_pointer:])

    return result

numbers = [38, 27, 43, 3, 9, 82, 10]
print("Original array:", numbers)
sorted_numbers = merge_sort(numbers)
print("Sorted array:", sorted_numbers)
