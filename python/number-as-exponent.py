from math import *
def numberExponent(A) :
    if A <= 1 : return True
    N = sqrt(A)
    i = 2
    while i <= N :
        product = 1
        while product < A :
            product = product * i
        if product == A :
            return True;
        i = i + 1
    return False