print("How many kilometers did you cycle today?")
milage = input()
km = float(milage)/1.60934
km = round(km, 2)
print(f"OK, your {milage}km ride was {km}mi cycled today")