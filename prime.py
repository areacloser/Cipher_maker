import math, random

def div_trial(num):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

def sieve(size):
    s = [True] * size
    s[0] = False
    s[1] = False

    for i in range(2, int(math.sqrt(size)) + 1):
        pointer = i * 2
        while pointer < size:
            s[pointer] = False
            pointer += i

    primes = []
    for i in range(size):
        if s[i] == True:
            primes.append(i)

    return primes

def rab_mill(num):
    if num % 2 == 0 or num < 2:
        return False
    if num == 3:
        return True
    s = num - 1
    t = 0
    while s % 2 == 0:
        s = s // 2
        t += 1
    for trials in range(5):
        a = random.randrange(2, num - 1)
        v = pow(a, s, num)
        if v != 1:
            i = 0
            while v != (num - 1):
                if i == t - 1:
                    return False
                else:
                    i += 1
                    v = (v ** 2) % num
    return True

LOW_PRIMES = sieve(100)

def judge(num):
    if (num < 2):
        return False

    for prime in LOW_PRIMES:
        if (num % prime == 0):
            return False

    return rab_mill(num)

def large_prime(size):
    while True:
        num = random.randrange(2**(size - 1), 2**(size))
        if judge(num):
            return num
