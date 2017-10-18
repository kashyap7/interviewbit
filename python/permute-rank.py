from math import factorial
def rank(A) :
	if len(A) == 1 : return 1
	sorted_list = sorted(A)
	n = len(sorted_list)
	fact = factorial(n)
	rank = 1
	for i in range(n) :
		fact = fact / (n - i)
		smaller_alpha = sorted_list.index(A[i])
		rank = rank + fact*smaller_alpha
		del sorted_list[smaller_alpha]
	return rank

print rank('acb')
print rank('string')