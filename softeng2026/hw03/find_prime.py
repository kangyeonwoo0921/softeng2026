def find_prime(n):
    primes = []
    for i in range(2, n + 1):
        is_prime = True
        for j in range(2, int(i**0.5) + 1):
            if i % j == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(i)
    return primes

num = int(input("숫자를 입력하세요: "))
prime_numbers = find_prime(num)
print(f"{num}의 소수: {prime_numbers}입니다.")