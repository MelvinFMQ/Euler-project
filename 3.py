upper_limit = int(600851475143 ** 0.5)
factors = []
multiple = 600851475143
for i in range(3, upper_limit, 2):
    while multiple % i == 0:
        factors.append(i)
        multiple = multiple / i
        if multiple == 1:
            print('Early finish')
            break
            #found all factors
            #without this, loop will continue to modulo 1 / i ( where i is larger than the greatest prime factor)
    
print(max(factors))

            
