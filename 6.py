#use arithmetic progression to find sum
sum_of_100 = (100 + 1) * (100 /2)
square_sum_of_100 = sum_of_100 ** 2


total = 0
for i in range(1, 101):
    total = i ** 2 + total

print(square_sum_of_100 - total)
    
