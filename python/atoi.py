def atoi(A):
    # first we get the first word which would be converted
    start = 0
    while start < len(A) and (A[start] != '-' and A[start].isdigit() == False) :
        start += 1
    num_string = A[start:]
    print "num_string-1", num_string
    if len(num_string) == 0 : return 0
    end = 0
    is_negative = (num_string[0] == '-')
    while end < len(num_string) and num_string[end].isdigit() == True :
        end += 1
    num_string = num_string[:end]
    print "num_string-2", num_string
    if len(num_string) == 0 :
        return 0
    output = 0
    power_10 = 1
    num_string = num_string[::-1]
    for i in num_string:
        output += power_10*int(i)
        power_10 *= 10
    
    if is_negative :
        return -1*output
    else :
        return output
A : "-88297 248252140B12 37239U4622733246I218 9 1303 44 A83793H3G2 1674443R591 4368 7 97"
print atoi(A)