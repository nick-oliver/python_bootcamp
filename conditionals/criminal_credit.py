criminal_record = True
good_credit = True

if good_credit and not criminal_record:
    print('Your are our target customer')
    print('You are eligible for a Loan')
else:
    print('You are not quite up to our standards')
    print('You are NOT eligible for a loan')
