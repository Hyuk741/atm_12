#잔액 초기화
balance = 1000

x=0
while True: #조건이 True면 계속반복합니다
    num = input("사용하실 기능을 선택해주세요 (1.입금, 2.출금, 3,영수증 보기, 4.종료): ")
#4를 입력하면 종료라는 출력메세지를 print()를 보여주는 코드 작성
#개발할때 최소한의 자원만 쓸수있도록 고려를 해보는게 좋다
    #2번 출금기능
    if num == '2':
        withdraw_amount = int(input('출금할 금액을 입력해주세요 : '))
        # if balance >= withdraw_amount:
        #     balance -= withdraw_amount
        withdraw_amount = min(balance, withdraw_amount) #결과값이 무조건 balance
        balance -= withdraw_amount
        print (f'출금하신 금액은 {withdraw_amount}원이고, 현재 잔액은 {balance}입니다.')

    #1번 입금 코드
    if num == '1':
        #얼마를 입금할 거야?
        deposit_amount = int(input("입금할 금액을 입력해주세요 : "))
        #balance
        #balance = balance + deposit_amount
        balance += deposit_amount
        print(f'입금하신 금액은{deposit_amount}원이고, 현재 잔액은{balance}입니다.')
        


    #4번 종료 코드
    if num == '4':
        print('종료')
        break

