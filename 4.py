#largest digits is 10^3^2 = 10^6 = 6 zeros
def is_palindrome(number):
    #number is datatype int
    #convert to string
    number = str(number)
    return number == number[::-1]


def largest(lower_limit):
    largest = 0
    i = 999
    #go in decending order to find the bigger palidromes first
    while i > lower_limit:
        j = 999
        while j > lower_limit:
            product = i * j
            if is_palindrome(product):
                #the latest palindrome found will have the larger lower limit.
                print("hi")
                if i > j:
                    lower_limit = j
                else:
                    lower_limit = i
                if product > largest:
                    largest = product
                    print(largest)
            j -= 1
        i -= 1
    print(largest)
                    
                
largest(0)
            
