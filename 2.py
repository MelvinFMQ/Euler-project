total = 2
fib1 = 1
fib2 = 2
fib3 = 0
while fib3 < 4000000:
    fib3 = fib1 + fib2
    fib1 = fib2
    fib2 = fib3
    if fib3 % 2 == 0:
        total += fib3
print(total)
