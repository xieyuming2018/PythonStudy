def quick_sort(lst):
    if len(lst) < 2:
        return lst
    else:
        refer_point = lst[0]
        greater = [element for element in lst[1:] if element > refer_point]
        lesser = [element for element in lst[1:] if element <= refer_point]
        return quick_sort(lesser) + [refer_point] + quick_sort(greater)

arr = [2,5,3,1,6,9,8,7]
print(quick_sort(arr))
