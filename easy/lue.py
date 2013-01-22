def bruteforce():
	input = raw_input();
	
	if input != '42':
		print input
		bruteforce()
	else:
		exit(0)
		
bruteforce()