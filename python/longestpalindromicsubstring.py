def longestpalin(A) :
	n = len(A)
	palin = n*[1]
	# palin stores the length of the longest palindromic string ending at so and so index
	print A
	for i in range(1,n):
		# check if we can append to the longest palindrome ending at the previous index
		temp = i - 1 - palin[i-1]
		print A[:i]
		print "i: ", i, "previous palindrome: ",A[i - palin[i-1]: i],"current char:", A[i]
		if i - 1 - palin[i-1] > 0 and A[i - 1 - palin[i-1]] == A[i] :
			palin[i] = palin[i-1] + 2
		else :
			# consecutive alphabets
			#print "blah: ", A[temp+1:i], A[temp+1]*palin[i-1]
			if A[i] == A[temp + 1] and A[temp + 1:i] == A[temp+1]*palin[i-1] :
				print "blah2: ", A[temp+1:i], A[temp]*palin[i-1]
				palin[i] = palin[i-1] + 1
	import operator
	index, value = max(enumerate(palin), key=operator.itemgetter(1))
	print index, value
	return A[index+1-value: index + 1]
print longestpalin("abaab")
print longestpalin("caccbcbaabacabaccacaaccaccaaccbbcbcbbaacabccbcccbbacbbacbccaccaacaccbbcc")

def longestpalinlimited(A):
	n = len(A)
	


