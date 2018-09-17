def selection_sort(lst):
    for i in range(len(lst)):
        min_element = i
        for j in range(i+1,len(lst)):
            if lst[j] < lst[min_element]:
                min_element = j
        lst[i],lst[min_element] = lst[min_element],lst[i]
    return lst

arr = [2,5,3,1,6,9,8,7]
print(selection_sort(arr))

