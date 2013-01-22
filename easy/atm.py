input = raw_input()

atmInput = input.split(' ')
atmAmounts = [float(x) for x in atmInput]

withdrawalAmount = atmAmounts[0]
startingBalance = atmAmounts[1]

if withdrawalAmount % 5 != 0:
	print '%.2f' % startingBalance
	exit(0)
else:
	endingBalance = startingBalance - withdrawalAmount - 0.50
	print '%.2f' % endingBalance
	exit(0)