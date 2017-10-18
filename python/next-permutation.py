"""
I need the next permutation. I would need find a pair (i,j) such that
A[j] > A[i] and i is of the lowest order
We swap the this i with the smallest integer greater than A[i] and has an index greater than i.
"""
X = [1,6,5,3,2]
Y = [9,6,4,8,7]
Z = [9,4,5,8,3,2,7]
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

print (X);          
print nextPermutation(X);           
print (Y);          
print nextPermutation(Y);           
print (Z);          
print nextPermutation(Z);           
