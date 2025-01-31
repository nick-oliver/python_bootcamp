price = 1000000
good_credit = True

if good_credit:
    down = price * .1
    print('Hi, we have checked your credit and it is good. You only need to pay 10% down.')
else:
    down = price * .2
    print('Hi, we have checked your credit and it is not so good. You need to pay 20% down.')
print(f'Your down payment is ${down}')
