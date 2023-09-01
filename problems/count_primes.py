# Leetcode Ques : 204 [Count Primes]

# Given an integer n, return the number of prime numbers that are strictly less than n.

# Sieve of Eratosthenes logic
def count_primes(n):
    primes = 0
    board = [0]*n
    for i in range(1,n):
        if board[i] == 0:  # 0 denote prime numbers
            primes += 1
            for j in range(i*i, n, i):
                board[j] = 1  # 1 denote composite numbers

    return primes

# Brute Force Method - TLE

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