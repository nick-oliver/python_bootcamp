# ask for age
age = input("How old are you?: ")
if age:
	age = int(age)
	if (age) >= 21:
		print("You can enter, but need a wristband!")
	elif (age) >= 18:
		print("You are good to enter and can drink.")
	else:
		print("You can't come in little one.")
else:
	print("Please enter an age.")