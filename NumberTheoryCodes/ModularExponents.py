# now we need to find a fast way to compute modular exponentiation
# first we can apply an efficient algorithm which is recursive one, by applying the following:
# since ab mod n = (a mod n)(b mod n) mod n
# so we cab compute b pow (e) by following these steps:
# 1- set c to 1
# 2- multiply c by b then take the mod immediately to avoid large numbers
# 3- repeat step 2 e times.
def fastModularExponentiation(b, e, n):
    c = 1
    for i in range(e):
        c = (c * b) % n

    return c


print(fastModularExponentiation(2, 10000, 1000000007))  # woooooow !!!

# okay this computed the results fast, but can we achieve faster one?
# yes we can, by using the following idea:
# consider the exponent is a 2 pow (k)
# so now we can reduce the number of computations by using powers of 2
# so for example if we want to compute 7 pow (128) so we can compute it in such way
# 7 pow (128) = 7 pow (64) * 7 pow (64)
# 7 pow (64) = 7 pow (32) * 7 pow (32)
# 7 pow (32) = 7 pow (16) * 7 pow (16)
# 7 pow (16) = 7 pow (8) * 7 pow (8)
# 7 pow (8) = 7 pow (4) * 7 pow (4)
# 7 pow (4) = 7 pow (2) * 7 pow (2)
# 7 pow (2) = 7 pow (1) * 7 pow (1)
# so we can compute it in O(log(e)) instead of O(e)
# and if e was not multiple of 2 pow (k) then you can represent e in the binary formate and use it as follows:
# let e = 13
#      |8 |4| 2| 1|
# ------------------
# 13 = |1 |1| 0| 1|
# so we can compute it as follows:
# 7 pow (13) = 7 pow (8) * 7 pow (4) * 7 pow (1) -> so 7 pow (8) and 7 pow(4) can be computed with pow of 2 and at the end
# we can multiply the result by 7 pow (1) which is 7.
# so we can compute it in O(2log(e)) atmost.
# so we can implement it as follows:


def fastModularExponentiationusingPowOf2(b, e, n):
    c = 1
    while(e > 0):
        if(e % 2 == 1):  # if the exponent is odd
            c = (c * b) % n  # multiply the result by the base
        b = (b * b) % n
        e //= 2

    return c


print(fastModularExponentiation(2, 10000, 1000000007))  # woooooow !!!
print(fastModularExponentiationusingPowOf2(
    9, 11, 13))  # woooooow !!!


# we have also a very interesting theorm which is called Fermat's Little Theorm which states that
# if p is a prime number and a is any integer then a pow (p) - a is divisible by p
# or in other words if (p) is prime then (a) pow (p - 1) is congruent to 1 mod p
# so we can use it to compute modular exponentiation in O(log(e)) time
# so we can implement it as follows:
def fastModularExponentiationusingFermatTheorm(b, e, n):
    # i know that a pow (n - 1) is congurant to 1 so we want to evaluate
    # so we want to compute the e module n - 1
    newExponent = e % (n - 1)

    # after that we need to compute the modular exponent using the newExponent
    return fastModularExponentiationusingPowOf2(b, newExponent, n)


print(fastModularExponentiation(2, 10000, 1000000007))  # woooooow !!!
print(fastModularExponentiationusingFermatTheorm(
    2, 10000, 1000000007))  # woooooow !!!


# also we can use fermat's little theorm to check if the number is prime or not
# so we can implement it as follows:
def isPrime(a, e):
    # we want to check whethere e is prime or not
    # to evaluate this , if e was not prime so it will violate the colloraly that
    # a pow (e) mod e congurant to a mod e
    return pow(a, e, e) == a


print(isPrime(2, 117))  # woooooow !!! -> not prime
print(isPrime(2, 31))  # woooooow !!! -> prime


# note that if the result if true this doesn't imply that the e is prime
print(isPrime(4, 91))  # woooooow !!! -> prime

# but if the result is false then it implies for sure that the e is NOT A PRIME.
print(isPrime(2, 117))  # woooooow !!! -> not prime
print(isPrime(2, 9))  # woooooow !!! -> not prime
