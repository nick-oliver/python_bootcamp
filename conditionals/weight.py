# COMPARISON OPERATORS

# user_weight_kg =
# print('The patients weight in kilograms is ' + str(user_weight_kg) + ' kilos ')

weight = input('How much do you weigh? ')
unit = input('(L)bs or (K)g ')

if unit.upper() == 'L':
    user_weight = int(weight) * 0.453
    print(f'Your weight in Kilograms is {user_weight}')
else:
    user_weight = int(weight) * 2.207
    print(f'Your weight in Pounds is {user_weight}')
