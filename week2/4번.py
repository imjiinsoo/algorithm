total_point = 0  # 누적 포인트

while True:
    money = int(input("투입한 돈 : "))
    if money == 0:
        print("감사합니다. 안녕히가세요")
        break

    price = int(input("물건값 : "))
    change = money - price
    print(f"거스름돈 : ₩{change} 원")

    coin_500 = change // 500
    change %= 500

    coin_100 = change // 100
    change %= 100

    coin_50 = change // 50
    change %= 50

    coin_10 = change // 10
    change %= 10

    total_coins = coin_500 + coin_100 + coin_50 + coin_10

    if total_coins >= 5:
        choice = input("동전의 개수가 많습니다. 포인트로 적립해 드릴까요? (Y or N)").lower()
        if choice == 'y':
            total_point += money - price
            print(f"{money - price} 포인트가 적립되었습니다. 현재까지의 누적포인트 : {total_point}")
        else:
            print(f"500원 동전의 개수 : {coin_500}")
            print(f"100원 동전의 개수 : {coin_100}")
            print(f" 50원 동전의 개수 : {coin_50}")
            print(f" 10원 동전의 개수 : {coin_10}")
    else:
        # 5개 미만이면 바로 동전 출력
        print(f"500원 동전의 개수 : {coin_500}")
        print(f"100원 동전의 개수 : {coin_100}")
        print(f" 50원 동전의 개수 : {coin_50}")
        print(f" 10원 동전의 개수 : {coin_10}")