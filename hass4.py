""" I won the grant for being the most awesome. This is how my reward is calculated.
My earnings start at $1 and can be doubled or tripled every month. 
Doubling the amount can be applied every month and tripling the amount can be applied every other month.
Write a program to maximize payments given the number of months by user. """

#Introducing the program
Welcome = "Congratulations!"
Welcome2 = "If you are using this program, that means you won the You-Are-Awesome award!"
print (100*"*")
print(format(Welcome,'^100s'))
print(format(Welcome2,'^100s'))
print (100*"*")
print("\n")
print("I am sure you are dying to know how much you won, let's compute!")
print("\n")

#Calculating and printing out the results.
amount = 1
months = int(input("For how many months did they say you will receive payments? "))
print("\n")
print("Here are the monthly installment amounts:")
print("\n")
for strategy in range(1,months+1,1):
	if strategy == 1:
		payment = "$"+str(amount)
		print("Month ",strategy, ":", payment.rjust(50))
	elif strategy %2 == 0:
		amount *= 2
		payment = "$"+str(amount)
		print("Month ",strategy, ":", payment.rjust(50))
	else:
		amount *= 3
		payment = "$"+str(amount)
		print("Month ",strategy, ":", payment.rjust(50))
