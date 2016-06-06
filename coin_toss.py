def coin_toss():
	import random
	heads = 0
	tails = 0
	for x in range(1, 5001):
		random_num = round(random.random())
		if (random_num == 0):
			heads += 1
		else:
			tails += 1
		print("Attempt #"+str(x)+": Throwing a coin... It's a "+("head" if random_num == 0 else "tail")+"! ... Got "+str(heads)+" head(s) so far and "+str(tails)+" tail(s) so far")
coin_toss()