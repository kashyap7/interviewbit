def gcd(A,B) :
    high = A if A > B else B
    low = A + B - high
    while low != 1 :
        if high % low == 0:
            return low
        else :
            k = high % low
            high = low
            low = k
    return low
print gcd(4,5)
print gcd(20,8)
print gcd(5,1)