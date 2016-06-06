def avg(arr):
	sum = 0
	for x in arr:
		sum += x
	return sum / len(arr)

print(avg([1,2,5,10,255,3]))