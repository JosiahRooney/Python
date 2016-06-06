def score_and_grades():
	for x in range(0,10):
		grade = input("Enter number grade: ")
		if ( type(grade) == 'int' ):
			print "Please enter a number grade."
			break
		if ( grade > 100 ):
			print "Please enter a number from 0 to 100"
			break
		if ( grade >= 90 ):
			output = "A"
		elif ( grade >= 80 ):
			output = "B"
		elif ( grade >= 70 ):
			output = "C"
		elif ( grade >= 60):
			output = "D"
		else:
			output = "F"
		print "Score: " + str(grade) + "; Your grade is " + output
score_and_grades()