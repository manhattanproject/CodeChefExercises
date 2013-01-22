testcases = int(raw_input())
list = []

def input():
	counter = 0
	
	if counter < testcases:
		list.append(raw_input())
		
	else:
		list.sort()
		output()

def output():
	for x in list:
		print list[x]
	exit(0)
	
input()