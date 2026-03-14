def check_even(num):
    if num % 2 == 0:
        return True
    else:
        return False
    
num = int(input("숫자를 입력하세요: "))

if check_even(num):
    print(f"{num} 는 짝수입니다.")
else:    
    print(f"{num} 는 홀수입니다.")