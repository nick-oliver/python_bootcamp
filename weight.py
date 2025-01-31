print("How many pounds do you weigh?")
poundage = input()
kg = float(poundage)*.453592
kg = round(kg, 2)
print(f"OK, you weigh {poundage}lbs, and that is {kg}kg")