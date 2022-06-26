# This prime generator uses the Sieve of Eratosthenes

import math

def create_leading_num_list(n):
    leading_num_list = []
    for i in range(2, n + 1):
            leading_num_list.append(i)
    return leading_num_list

def check_prime(n):
    isPrime = False
    if n > 1:
        for i in range(1, math.floor(math.sqrt(n)) + 1):
            if math.gcd(i, n) != 1:
                return isPrime
        isPrime = True
    return isPrime

def generate_prime_list(n):
    prime_list = []
    if n > 1:
        prime_list = create_leading_num_list(n)
        i = 0
        while i < len(prime_list): 
            if check_prime(prime_list[i]):
                if len(prime_list) > i + 1:
                    j = i + 1
                    while j < len(prime_list):
                        if prime_list[j] % prime_list[i] == 0:
                            prime_list.remove(prime_list[j])
                        j += 1
                i += 1
    print(prime_list)