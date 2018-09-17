def buble_sort(lst):
    for i in range(len(lst)):
        swaped = False
        for j in range(len(lst)-1):
            if lst[j] > lst[j+1]:
                swaped = True
                lst[j],lst[j+1] = lst[j+1],lst[j]
        if not swaped: break
    return lst

arr = [2,5,3,1,6,9,8,7]
print(buble_sort(arr))