def printFizzBuzz(last_number):
	for x in range(1,last_number+1):
		if x % 15 == 0:
			print("Fizz Buzz")
		elif x % 3 == 0:
			print("Fizz")
		elif x % 5 == 0:
			print("Buzz")
	print("Sequence Complete")

printFizzBuzz(60)