def quick_sort_2(arr):
    n = len(arr)
    if n <= 1:
        return arr

    pivot = arr[n//2]
    leftArr, rightArr = [], [],

    for num in arr:
        if num < pivot:
            leftArr.append(num)

        elif num > pivot:
            rightArr.append(num)

    return quick_sort_2(leftArr) + [pivot] + quick_sort_2(rightArr)

arr = [5,3,8,4,9,1,6,2,7]
print("before quick_sort_2: ", arr)
print("after  quick_sort_2: ", quick_sort_2(arr))