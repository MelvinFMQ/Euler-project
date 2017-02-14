import timeit
def gen_primes():
    n = 100001
    upper_limit = n
    lower_limit = 2 
    primes = [2]
    count = 1
    while count < n:
        a = [True] * (upper_limit - lower_limit)
        for prime in primes: #remove previous prime's multiplies
            nearest_multiple = (lower_limit // prime + (lower_limit % prime != 0)) * prime #round up
            for j in range(nearest_multiple, upper_limit, prime):
                a[j-lower_limit] = False    
        for i, is_prime in enumerate(a):
            if is_prime: #remove new prime's multiples
                actual_number = lower_limit + i
                for j in range(actual_number ** 2, upper_limit, actual_number):
                    a[j - lower_limit] = False
                primes.append(lower_limit + i)
                count += 1
                if count == n:
                    break

        #large at the start is better to reduce the double iterations.
        #slow down as approaches the nth prime.
        lower_limit = upper_limit
        upper_limit = upper_limit + int(upper_limit ** 0.5)
    print(primes[-1])


def gen_prime_div():
    n = 100001
    primes = [2]
    number_to_test = 3
    count = 1
    while count < n:
        is_prime = True
        for prime in primes:
            if prime > int(number_to_test ** 0.5):
                break
            if number_to_test % prime == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(number_to_test)
            count += 1
        number_to_test += 2
    print(primes[-1])

#print(timeit.timeit(gen_primes, number= 1))
#print(timeit.timeit(gen_prime_div, number = 1))
print(timeit.timeit(gen_primes, number = 1))


