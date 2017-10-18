def solve(A, c):
    # Now dp of C
    # if len(C) == 0 :
    #   return 0 
    # elif len(C) == 1 :
    #   i = 0
    #   for i in range(len(A)) :
    #       if A[i] > C:
    #           break
    #   return i
    # else :
# Jackass please pay good attention to the solution at the least
    if c//10 == 0 and A[0] == 0 :
        count = 0
        l = 0
        while l < len(A) and A[l] < c:
            count += 1;
            l += 1
        return count
    C = []
    if c == 0 :
        return 0
    else :
        while(c):
            C.append(c%10)
            c //= 10
    C = C[::-1]
    lower = [0]*10
    dp = [0]*(len(C))
    for i in range(10) :
        j = 0;
        while j < len(A) and A[j] < i:
            lower[i] += 1;
            j += 1
#   print lower
    possible = False
    for i in range(len(C)) :
        if i == 0:
            dp[0] = lower[C[0]]
            if A[0] == 0 : dp[0] -= 1
            for j in range(len(A)) :
                if C[0] == A[j] :
                    possible = True
                    break
            continue
        else :
            dp[i] += dp[i - 1]*len(A)
            if possible == True :
                dp[i] += lower[C[i]]
                possible = False
                for j in range(len(A)) :
                    if C[i] == A[j] :
                        possible = True
                        break
    return dp[len(C)-1]
A = [0,1,2,5]
c = 21
print solve(A, c)
B = [0,1,5]
c = 2
print solve(B,c)




