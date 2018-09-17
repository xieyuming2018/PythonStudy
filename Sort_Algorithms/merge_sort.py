def merge_sort(lst):
    length = len(lst)
    if length > 1:
        midpoint = length // 2
        left_half = merge_sort(lst[:midpoint])
        right_half = merge_sort(lst[midpoint:])
        i = 0
        j = 0
        k = 0
        left_length = len(left_half)
        right_length = len(right_half)
        while i < left_length and j < right_length:
            if left_half[i] < right_half[j]:
                lst[k] = left_half[i]
                i += 1
            else:
                lst[k] = right_half[j]
                j += 1
            k += 1
        while i < left_length:
            lst[k] = left_half[i]
            i += 1
            k += 1
        while j < right_length:
            lst[k] = right_half[j]
            j += 1
            k += 1
    return lst

arr = [2,5,3,1,6,9,8,7]
print(merge_sort(arr))