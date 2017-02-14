import timeit

def gen_primes():
    #n represents the nth prime
    n = 1000
    multiples = []
    primes = []
    step = 10
    lower = 2
    upper = lower * step
    multiples = multiples + [i for i in range(lower, upper + 1)]
    while len(primes) < n:
        new_prime = multiples[0] #first element is a prime
        primes.append(new_prime)
        max_multiplication = upper // new_prime
        min_multiplication = lower // new_prime 
        for multiplicator in range(min_multiplication, max_multiplication + 1):
            try:
                multiples.remove(multiplicator * new_prime)
            except ValueError:
                pass
        if len(multiples) == 0:
            #all multiples for this range has been removed, then move on to next range
            lower = upper
            upper = lower * step 
            multiples = multiples + [i for i in range(lower, upper)]
            removed_multitples = []
            for prime in primes:
                max_multiplication = upper // prime
                min_multiplication = lower // prime 
                for multiplicator in range(min_multiplication, max_multiplication + 1):
                    product = multiplicator * prime  
                    try:
                        multiples.remove(product)
                    except ValueError:
                        pass
    print(primes[-1])



def generate_multiplicator(previous_primes, current_prime, lower, upper):
    #generate
    pass

def gen_prime_basic():
    limit = 1000000
    a = [True] * limit                          # Initialize the primality list
    a[0] = a[1] = False

    for (i, isprime) in enumerate(a):
        if isprime:
            yield i
            for n in xrange(i**2, limit, i*2):     # Mark factors non-prime
                a[n] = False
    print(a[-1])



#gen_prime_basic()

def gen_prime_div():
    n = 1000000
    primes = [2]
    number_to_test = 3
    while number_to_test < n:
        is_prime = True
        for prime in primes:
            if prime > int(number_to_test ** 0.5):
                break
            if number_to_test % prime == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(number_to_test)
        number_to_test += 2
    print(primes[-1])

#print(timeit.timeit(gen_primes, number= 1))
print(timeit.timeit(gen_prime_div, number = 1))
print(timeit.timeit(gen_prime_basic, number = 1))


#mulitiplicator 1,2,3,4,5,6
#2 [2, 3, 5, 7, 9...]
#mulitiplicator 3,5,7,9,11,13,15
#3 [2, 3, 5, 7, 11, 13...
 #5, 7, 11 , 13



