def draw_stars(list):
	for i in list:
		if isinstance(i, basestring):
			for x in i.lower()[0]:
				print x * len(i)
		else:
			print "*" * i
draw_stars([4, "Tom", 1, "Michael", 5, 7, "Jimmy Smith"])