def nextPermutation(A):
    n = len(A);
    i = n - 1;
    while ( i > 0) and (A[i - 1] > A[i]) :
        i = i - 1;
    if i == 0 :
        return 0;
    else :
        min_i = i;
        for j in range(i,n) :
            if A[j] > A[i-1] :
                if A[min_i] > A[j] :
                    min_i = j
        #swap i-1 and min_i
        k = A[i-1]
        A[i-1] = A[min_i]
        A[min_i] = k
        # sort the array from i to end of the array
        A[i:] = sorted(A[i:])
        return A
def next_permutation(arr):
    # Find non-increasing suffix
    i = len(arr) - 1
    while i > 0 and arr[i - 1] >= arr[i]:
        i -= 1
    if i <= 0:
        return False
    
    # Find successor to pivot
    j = len(arr) - 1
    while arr[j] <= arr[i - 1]:
        j -= 1
    arr[i - 1], arr[j] = arr[j], arr[i - 1]
    
    # Reverse suffix
    arr[i : ] = arr[len(arr) - 1 : i - 1 : -1]
    return True
# @param A : list of integers
# @param B : integer
# @param C : integer
# @return an integer
def solve(A, B, C):
    lenC = len(list(str(C)))
    print len(A), B, lenC
    if B > lenC : return 0
    from itertools import combinations_with_replacement
    from math import pow
    if B == lenC :
        k = combinations_with_replacement(A,B)
        count = 0
        for i in k:
            comb_list = list(i)
            value = int(''.join(map(str, comb_list)))
            max_value = int(''.join(map(str, comb_list[::-1])))
            # if value < C and value <= max_value : count = count + 1
            done = True
            #print value
            while value < C and value <= max_value and done:
                print comb_list
                if value/pow(10,B-1) >= 1 or (B == 1 and value == 0):
                    count = count + 1
                done = next_permutation(comb_list);
                value = int(''.join(map(str, comb_list)))
        return count
    else :
        n = len(A)
        if A[0] == 0 :
            return int((n-1)*pow(n,B-1))
        else : return int(pow(n,B))
A = [0,1,2,5]
B = 2
C = 324
print solve(A, B, C)