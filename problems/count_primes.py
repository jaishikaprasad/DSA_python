def count_primes(n):
    primes = 0
    for num in range(1,n):
        if num > 1:
            for i in range(2, num):
                if num % i == 0:
                    break
            else:
                primes += 1

    return primes

print(count_primes(10))