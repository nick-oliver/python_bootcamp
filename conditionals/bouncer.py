# # ask for age
# age = input("How old are you?: ")
# if age:
# 	age = int(age)
# 	if (age) >= 18 and (age) < 21:
# 		print("You can enter, but need a wristband!")
# 	elif (age) >= 21:
# 		print("You are good to enter and can drink.")
# 	else:
# 		print("You can't come in little one.")
# else:
# 	print("Please enter an age.")

# refactored and simpler
# ask for age
age = input("How old are you?: ")
if age:
	age = int(age) #converts age variable to an integer
	if (age) >= 21: #evaluated first - if true, evaluations stop
		print("You are good to enter and can drink.")
	elif (age) >= 18: #if previous evaluation fails, this is evaluated next
		print("You can enter, but need a wristband!")
	else: #if previous 2 evaluations fail, then age is, by default, less than 18
		print("You can't come in little one.")
else: #In the event no age is entered
	print("Please enter an age.")