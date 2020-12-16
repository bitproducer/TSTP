def fizzBuzz(counter):											# create function
	for i in range (1,counter+1):								# run for 'counter' times
		if i % 3 == 0 and i % 5 == 0:							# check for multiplies of 3 and 5, has to be first otherwise it would not come up, print 'FizzBuzz'
			print ('FizzBuzz')
		elif i % 3 == 0:										# check for multiplies of 3, print 'Fizz'
			print ('Fizz')
		elif i % 5 == 0:										# check for multiplies of 5, print 'Buzz'
			print('Buzz')
		else:													# for all other numbers print the number
			print (i)

inputCounter = int(input('please set a number: '))
fizzBuzz(inputCounter)
