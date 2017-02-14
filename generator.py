def generator():
    for i in range(10):
        yield i
        for n in xrange(1,10,1):
            print(n)
for i in generator():
    print(i)
    
