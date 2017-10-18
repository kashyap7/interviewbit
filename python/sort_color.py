def sortColors(A) :

	A = [1] + A
	start_1 = 0
	end_1 = 0
	n = len(A)
	iter_2 = n -1
	while iter_2 > 0 and A[iter_2] == 2 :
		iter_2 -= 1
	if iter_2 == 0:
		return A[1:]

	while (iter_2 >= end_1) :

		# be vary of the terminating condition
		print "iter_2:", iter_2, "|start_1: ", start_1, "|end_1: ", end_1
		print A
		if A[end_1] == 1 :
			end_1 += 1
		elif A[end_1] == 2:
			A[end_1] = A[iter_2]
			A[iter_2] = 2
			while iter_2 >= end_1 and A[iter_2] == 2:
				iter_2 -= 1
		else :
			A[end_1] = 1
			A[start_1] = 0
			start_1 += 1
	del A[start_1]
	return A
A = [0,1,2,0,1,2]
print sortColors(A)
B = [ 1, 0, 0, 1, 1, 0, 0, 2, 1, 2, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 0, 0, 2, 0, 2, 2, 2, 0, 0, 1, 1, 1, 2, 2, 0, 2, 2, 2, 2, 2, 1, 1, 2, 2, 2, 1, 2, 1, 1, 0, 0, 1, 2, 1, 1, 0, 1, 0, 2, 0, 2, 1, 0, 1, 1, 0, 0, 1, 2, 0, 1, 0, 2, 1, 0, 1, 0, 1, 0, 1, 2, 2, 2, 0, 1, 1, 0, 2, 2, 2, 0, 0, 0, 0, 1, 1, 2, 1, 0, 1, 0, 1, 2, 2, 1, 0, 2, 0, 0, 1, 2, 1, 0, 2, 1, 0, 2, 0, 2, 1, 1, 1, 1, 1, 0, 1, 2, 0, 0, 1, 0, 1, 2, 0, 1, 1, 2, 1, 0, 2, 0, 0, 0, 2, 0, 1, 0, 2, 1, 1, 0, 1, 2, 1, 0, 0 ]
print sortColors(B)
