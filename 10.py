def sum_prime(n):
    primes = [True] * n
    primes[0] = primes[1] = False
    total = 0
    for i, is_prime in enumerate(primes):
        if is_prime:
            for multiple in range(i**2, n, i):
                primes[multiple] = False
            total += i
            #print(i)
    return total

print(sum_prime(2000000))
        
