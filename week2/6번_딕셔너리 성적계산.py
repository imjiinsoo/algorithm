d_sj = {"국어":0, "영어":0, "수학":0}

def f1(menu):
    if menu == 1:
        d_sj["국어"] = int(input("국어점수는?"))
        d_sj["영어"] = int(input("영어점수는??"))
        d_sj["수학"] = int(input("수학점수는?"))
    elif menu == 2:
        sub = input("수정할 과목은?")
        score = int(input("몇점으로 수정할까요?"))
        d_sj[sub]=score

def f2(d_sj):
    hap = 0
    for i in list(d_sj.keys()):
        hap += d_sj[i]
    return hap/3

def f3(avg):
    print("성적 계산: ")
    print("평균 점수: %.2f점" %avg)


print("성적을 입력하세요! ")
while True:
    menu = int(input("1)점수입력 2)점수수정 3)종료(0입력)"))
    if menu == 0: break
    elif menu != 1 and menu != 2 and menu != 0:
        print("잘못 입력하셨습니다")
    else: f1(menu)
print(d_sj)
f3(f2(d_sj))