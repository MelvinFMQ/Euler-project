def gen_prime(n):
    #generate primes until n
    #using seave
    number_pool = [i for i in range(2,n + 1)]
    primes = [2]

    for i in primes:
        j = 1
        while j * i <= n:
            try:
                number_pool.remove(j * i)
            except ValueError:
                pass
            j += 1
        if number_pool == []:
            return primes
        primes.append(number_pool[0])
    

def factorise(n):
    primes = gen_prime(n)
    prime_factors = []
    for prime in primes:
        while n % prime == 0:
            prime_factors.append(prime)
            n  = n// prime
    return prime_factors

def generate_product(a):
    product = 1
    for num in a:
        product = num * product
    return product


 
minimum_primes = gen_prime(20) #get unique primes
minimum_product = generate_product(minimum_primes)
for i in range(2, 21):
    if minimum_product % i != 0: #cannot be evenly divisible --> add more primes
        print("not divisible evenly!", i)
        individual_factors = factorise(i)
        print(individual_factors)
        unique_factors = []
        for factor in individual_factors:
            if factor not in unique_factors:
                unique_factors.append(factor)
        print('unique', unique_factors)
        for factor in unique_factors:
            inside = minimum_primes.count(factor)
            required = individual_factors.count(factor)
            print("inside", inside, "required", required)
            for i in range(required - inside):
                minimum_primes.append(factor) #insert to required primes
                print("inserting, " , factor)
        minimum_product = generate_product(minimum_primes)

print(minimum_product)
print(minimum_primes)
        

    
