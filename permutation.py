def gen_permutation(previous, a):
    #assume all unique
    if a == []:
        print(previous)
    for i in range(len(a)):
        #select the first option 
        gen_permutation(previous + str(a[i]), a[:i] +a[i + 1:])

gen_permutation("", [1,2,3,4])
