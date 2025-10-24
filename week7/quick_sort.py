def quick_sort(A,left,right):
    if left < right:
        # partition을 호출하면 high값이 나오고 그게 중심이 된다
        mid = partition(A, left, right)

        quick_sort(A, left, mid-1)
        quick_sort(A, mid+1, right)

def partition(A, left, right):
    low = left + 1
    high = right
    pivot = A[left]
    while (low <= high):
        # low는 pivot보다 작으면 맞는거니까 크기 비교하면서 한칸씩 오른쪽으로 이동
        while low <= right and A[low] < pivot:
            low += 1

        # high는 pivot보다 크면 맞는거니까 크기 비교하면서 한칸씩 왼쪽으로 이동
        while high >= left and A[high] > pivot:
            high -= 1

        if low < high:
            A[low], A[high] = A[high], A[low]
    A[left], A[high] = A[high], A[left]
    print("회전 진행 중:         ", A)
    return high

data = [45, 12, 23, 50, 18, 25, 40, 30, 27, 35]
print("before quick_sort: ", data)
quick_sort(data, 0, len(data)-1) # (리스트, 맨 처음 인덱스, 젤 마지막 인덱스)
print("after  quick_sort: ", data)