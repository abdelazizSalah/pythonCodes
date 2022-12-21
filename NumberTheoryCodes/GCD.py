# this file contains some algorithms for computing the GCD of two numbers.
# 1- the Naive algorithm: here we get the minimum of the two numbers and stay subtracting 1 from it till we find the
# number that divides both of them
# its problem is that if the numbers were very large and they have small gcd, then it will take high complexity O(min(a,b))
def NaiveAlgorithmGCD(a, b):
    if(a < 0 | b < 0):
        return max(a, b)
    mn = min(a, b)
    for i in range(mn, 0, -1):
        if(a % i == 0 and b % i == 0):
            return i


# the idea is here, for such large numbers this algorithm will take very long time to compute the result, it will
# compute it right, but it is very simple so it is very slow.
print(NaiveAlgorithmGCD(54320543590223053250, 1453234276239426509362))


# 2- Euclid's algorithms is depending on his lemma which says:
# d|a and d|b iff d|a-b and d|b
# try to prove it to see that it works.
# this is better because we instead of subtracting only 1, we are subtracting b from a or a from b
# so this will slightly increase the performance but it also faces the problem that it is liner and
# takes complexity O(min(max(a,b) - min(a,b)))
# so we can get a better version of the Naive algorithms which can be implemented as follows:
def betterVersionOfNaiveGCD(a, b):
    if(a < 0 or b < 0):
        return max(a, b)

    while(a > 0 and b > 0):
        if(a > b):
            a -= b
        elif (b >= a):
            b -= a

    return max(a, b)


# here if used the same example as before we will find that it has computed it faster, but still it is slow
print(betterVersionOfNaiveGCD(54320543590223053250, 1453234276239426509362))

# but if used example like this we will find that it has a very bad complexity,
# and as the difference between a and b decreses,
# the complexity will increase
print(betterVersionOfNaiveGCD(54320543590223053250, 7))


# so we tried to avoid subtraction and go for better analysis which depends on the division
# which really enhances the complexity alot, as we just need to get the remainder of the number
# to get the number that when we subtract a from it we can get 0 or less
# so we computed this version
def EcluidsBestVersionGCD(a, b):
    if(a < 0 or b < 0):
        return max(a, b)

    while (a > 0 and b > 0):
        if(a > b):
            a %= b
        else:
            b %= a

    return max(a, b)


# here we will see that this algorithm has solved the problem of both 1st and 2nd algorithms
# and it is very fast actually.
print(EcluidsBestVersionGCD(54320543590223053250, 7))
print(EcluidsBestVersionGCD(54320543590223053250, 1453234276239426509362))


# the compact version of the ecludies algo is here
# this is fast because the remainder of a % b is always < a/2 so we remove half of the result
# each iteration so we can get the results very fast so the
# complexity here is O(lg(2)(a) + lg(2)(b))
def recersiveEcludieAlgo(a, b):
    if(b <= 0):
        return a

    return recersiveEcludieAlgo(b, a % b)


print(recersiveEcludieAlgo(54320543590223053250, 7))
print(recersiveEcludieAlgo(54320543590223053250, 1453234276239426509362))


# now we want to apply the extending of euclid's algorithms
# this is applicable by formating gcd(a,b) = (int)a + (int)b
# so this function is used to return this two integers and return the gcd too
def extended_gcd(a, b):
    assert a >= b and b >= 0 and a+b > 0


print(extended_gcd(391, 299))


# now lets try the lcm which is the least common multiplier
# which is the least integer or the minimum integer that can be divided by both a and b

# this is the simplest way to compute the LCM but it is very exahstive and time consuming
def naiveLCM(a, b):
    assert a > 0 and b > 0
    for d in range(1, a * b + 1, 1):
        if(d % a == 0 and d % b == 0):
            return d


print(naiveLCM(12, 26))

# a better way to compute the lcm is through the gcd by this equation
# lcm(a, b) = (a*b) / gcd(a, b)


def LCMUsingGCD(x, y):
    assert x > 0 and y > 0
    return (x * y) // EcluidsBestVersionGCD(x, y)


print(LCMUsingGCD(12, 26))
