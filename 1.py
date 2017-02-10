list_of_natural_numbers = []
for i in range(1,1000):
    if i % 3 ==0 or i % 5 == 0:
        list_of_natural_numbers.append(i)

print(sum(list_of_natural_numbers))
