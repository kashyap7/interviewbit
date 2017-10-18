def count(A,B) :
	output = 0
	for word in B :
		output += A.count(word)
	return output
def solve(A,B) :
	goodWords = A.split("_")
	return sorted(B,key =lambda x: count(x,goodWords), reverse=True)
S = "cool_ice_wifi"
R = ["water_is_cool", "cold_ice_drink", "cool_wifi_speed"]
print solve(S, R)