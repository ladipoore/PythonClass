""" This program calculates the insurance premium paid based on age and accident history"""
BaseCost = 50.00
age = int(input("How old are you?: "))
if age >15:
	if age < 25:
		TotalCost = BaseCost + 100
	elif age < 35:
		TotalCost = BaseCost + 20
	else:
		TotalCost = BaseCost

	accidents = int(input("How many accidents have you been involved in in the last 5 years: "))
	if accidents <0:
		print("Your entry is invalid. Good bye!")
	elif accidents < 2:
		print("Your total monthly insurance premium is: $%.2f" % TotalCost)
	elif accidents == 2:
		TotalCost = TotalCost + (accidents*40)
		print("Your total monthly insurance premium is: $%.2f" % TotalCost)
	elif accidents < 5:
		TotalCost = TotalCost + (accidents * 60)
		print("Your total monthly insurance premium is: $%.2f" % TotalCost)
	else:
		print("Sorry! We cannot provide you with auto insurance.\nTry Geico")
else:
	print("You are not old enough to drive. Good bye!")
