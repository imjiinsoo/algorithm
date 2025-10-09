def insert_sort(A):
    n = len(A)
    for i in range(1,n):
        key = A[i] # 1번 인덱스부터. 0번 인덱스는 이미 정렬됐다고 가정
        j = i - 1 # i 왼쪽부터(i왼쪽이 정렬된 것들)
        while j >= 0 and A[j] > key: # j가 0보다 작아지면 끝, key랑 j번 인덱스 값이랑 비교(J는 정렬된 애들 중 하나)
            A[j+1] = A[j]
            j -= 1
        A[j+1] = key
        printStep(A, i)

def printStep(arr, val):
    print(" Step %2d = " % val, end="")
    print(arr)

data = [5,3,8,4,9,1,6,2,7]
print("Original  : ", data)
insert_sort(data)
print("Insertion : ", data)
