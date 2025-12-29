def counting_sort2(A):
    # 알파벳은 26글자이므로 크기 26의 배열 생성
    MAX_VAL = 26
    count = [0] * MAX_VAL
    output = [0] * len(A)

    for char in A:
        # 대소문자 구분 없이 정렬하기 위해 모두 대문자로 생각하고 인덱스 계산
        # ord('A')는 65. A 이후로 66,67 ~
        idx = ord(char.upper()) - ord('A')
        count[idx] += 1

    for i in range(1, MAX_VAL):
        count[i] += count[i - 1]

    for i in range(len(A)) :
        char = A[i]
        idx = ord(char.upper()) - ord('A')  # 동일하게 인덱스 계산

        output[count[idx] - 1] = char
        count[idx] -= 1

    return output


# 테스트 데이터
data = ['a', 'F','C', 'c', 'Z', 'y', 'd', 'D']
print(counting_sort2(data))