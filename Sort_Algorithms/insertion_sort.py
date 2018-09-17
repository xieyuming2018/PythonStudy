def insertion_sort(lst):
    for index in range(1, len(lst)):
        while 0 < index and lst[index] < lst[index - 1]:
            lst[index], lst[index - 1] = lst[index - 1], lst[index]
            index -= 1
    return lst

arr = [2,5,3,1,6,9,8,7]
print(insertion_sort(arr))