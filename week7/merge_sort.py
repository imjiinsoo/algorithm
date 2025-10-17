# merge_sort main(젤 작은 단위로 만들고 재귀로 다시 올라오면서 정렬)
def merge_sort(data):
    # 길이가 1이면 그냥 그대로 리턴
    if len(data) <= 1:
        return data

    # 자를 중앙 위치
    mid = len(data) // 2
    left = data[:mid]
    right = data[mid:]

    # 길이가 1이 될때까지 merge_sort 재귀 호출
    left = merge_sort(left)
    right = merge_sort(right)

    return merge(left, right)



def merge(left,right):
    # left, right 머지한 리스트를 담을 빈 리스트
    result = []

    # 인덱스 0으로
    i=j=0

    # 더 작은 값 앞에서부터 비교하고 더 작은 리스트의 i,j 값 하나씩 올리면서 쭉 비교
    while len(left) > i and len(right) > j:
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # 마지막에 하나는 다 소거된 리스트일텐데 그냥 둘 다 현재 인덱스(i혹은 j)부터 result에 나머지 extend하기
    result.extend(left[i:])
    result.extend(right[j:])

    return result

data = [38, 27, 43, 3, 9, 82, 10]

print(data)
print(merge_sort(data))