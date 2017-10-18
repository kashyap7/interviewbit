def isPalindrome(A):
    num_list = []
    while int(A) > 0 :
        num_list.append(A%10)
        A = A/10
    while len(num_list) > 1 and A[0] == A[-1]:
        del A[0]
        del A[-1]
    if len(A) > 1 :
        return False
    else :
        return True
print isPalindrome(1211)
print isPalindrome(121)
