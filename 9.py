#by combining a^2 + b ^2 = c^2
#and a +b + c = 1000
#get eqn b = (1000 ** 2 / (2* a -2000)) + 1000
#try values of a where 1 - 1000 
arr = []
for a in range(1000):
    b = (1000 ** 2 / (2* a -2000)) + 1000
    if b > 0  and b // 1 == b: #check for positive number and whole number
        arr.append('a ' + str(a) + ' ' + 'b ' + str(b))
print(arr)
