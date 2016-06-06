def oddEven():
	for x in range(0,2001):
		print "Number is " + str(x) + '. This is an ' + ("even number." if x % 2 == 0 else "odd number.")
oddEven()