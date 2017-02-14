#largest digits is 10^3^2 = 10^6 = 6 zeros
def is_palindrome(number):
    #number is datatype int
    #convert to string
    number = str(number)
    return number == number[::-1]


#x --> outer factor
#y --> inner factor

#algorithm starts from largest 3 digit number first to
#generate bigger palindromes (but not biggest) first.
#this is because the first factor is larger when we start from the top.
#e.g x * y = product, if x starts at 999 --> it will test 999 * y, 998 * y , 997 * y...
#which generates larger palindromes compared to 1 * y, 2 * y, 3 *y .

#when algorithm finds a palindrome, the smaller factor will be the lower limit for the inner loop.
#this is because to generate a larger pallindrome, future inner factor is required to be larger
#than the recently found inner factor due to the outer factor decreasing
#e.g x * y = product, x is decreasing. For product to increase, y must be larger.
#reduces numbers in inner loop required to check 



#when the algorithm finds a palindrom, the smaller factor will also be the lower limit for the outer loop.
#this is because we know that numbers smaller than the smaller factor has been combined with the larger other factors,
#due to decreasing nature of the outer loop. Do not need to test smaller other factor as it will result in smaller products. 
#e.g assume no other palindrome found, and these factors actually form palindromes. We are just checking that the alorithm is exhausive.
#902 * 18 = palindrome (18 lower limit) 
#...
#901 * 19 = palindrome (19 lower limit)
#..
#900 * 18 = palindrome (will not be generated, but this product will be smaller so does not need to be tested)
#..
#19 * 901 = palindrome (19 lower limit) 
#..
#18 * 902 = palindrome (will not be generated again, but already tested so alorithm is exhausive)
#reduce numbers in outer loop required to check


def largest(lower_limit):
    largest = 0
    i = 999
    #go in decending order to find the bigger palidromes first
    while i > lower_limit:
        j = 999
        while j > lower_limit:
            product = i * j
            if is_palindrome(product):
                #the latest palindrome found will have a larger lower limit.
                print("hi")
                if i > j and j > lower_limit:
                    lower_limit = j
                    print(lower_limit)
                elif j > i  and i > lower_limit:
                    lower_limit = i
                    print(lower_limit)
                if product > largest:
                    largest = product
                    print(largest)
            j -= 1
        i -= 1
    print(largest)
                    
                
largest(0)
            
