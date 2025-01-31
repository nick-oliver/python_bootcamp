course = 'Python for Beginners'
print(course.title())

patient_name = input('What is the patients name?: ')
birth_year = input('Birth year: ')
favorite_color = input('What os your favorite color? ')
user_weight_lbs = input('How much do you weigh in pounds? ')
user_weight_kg = int(user_weight_lbs) * 0.45
patient_age = 2021 - int(birth_year)
existing_patient = True
print(len(course))

print(course.lower())
print(course.upper())
print(course.find('n'))
print(course.replace('Beginners', 'Old Beginners'))
print('Beginners' in course)
print('The patients name is ' + patient_name)
print('The patients age is ' + str(patient_age))
print(patient_name + ' likes ' + favorite_color)
print('The patients weight in kilograms is ' + str(user_weight_kg) + ' kilos ')

first = 'Nick'
last = 'Oliver'
msg = f'{first} [{last}] is working on being a coder'
print(msg)

price = 1000000
good_credit = True

if good_credit:
    down = price * .1
    print('Hi, we have checked your credit and it is good. You only need to pay 10% down.')
else:
    down = price * .2
    print('Hi, we have checked your credit and it is not so good. You need to pay 20% down.')
print(f'Your down payment is ${down}')


LOGICAL OPERATORS

criminal_record = True
good_credit = True

if good_credit and not criminal_record:
    print('Your are our target customer')
    print('You are eligible for a Loan')
else:
    print('You are not quite up to our standards')
    print('You are NOT eligible for a loan')

CONDITIONAL OPERATORS

name = 'Arugliuglbougbuliglyfliglugilyfyudfi;uglifylydddd'

if len(name) >= 3 and len(name) < 50:
    print(name)
else:
    print("The name must have at least 3 and be no greater than 50 characters")


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

# While Loops
i = 1
while i <= 5:
    print('*' * i)
    i = i + 1
print('Done')


# GUESSING GAME

secret_number = 9
guess_count = 0
guess_limit = 3
while guess_count < guess_limit:
    guess = int(input('Guess: '))
    guess_count += 1
    if guess == secret_number:
        print('You Won!!')
        break
else:
    print('Sorry, you did not guess the number')


# CAR GAME

command = ""
started = False
while True:
    command = input("> ").lower()
    if command == "start":
        if started:
            print('Car is already started!!')
        else:
            started = True
            print('The Car has Started!!')
    elif command == "stop":
        if not started:
            print("The car is already stopped")
        else:
            started = False
            print('The Car has Stopped!!')
    elif command == "help":
        print("""
start - to start the car
stop - to stop the car
quit - to exit
        """)
    elif command == 'quit':
        break
    else:
        print("Sorry, I don't understand that")

FOR LOOP

prices = [10, 20, 30, 46, 53, 66]
total = 0
for price in prices:
    total += price
print(f'The Total is: {total}')

#extra credit
average = total/len(prices)
print(f"The average cost is {average}")

NESTED LOOPS

# Creates a set of coordinates
for x in range(5):
    for y in range(4):
        print(f'({x}, {y})')

# exercise - final version creates an 'L'
numbers = [2, 2, 2, 2, 6]
for number in numbers:
    output = ''
    for count in range(number):
        output += 'x'
    print(output)


# LISTS
names = ['John', 'Bob', 'Nick', 'Caroline', 'Sherie', 'Ruby']
print(names[:5])

# find the largest number
numbers = [2, 3, 7, 2, 8, 43, 8, 10]
max = numbers[0]

for number in numbers:
    if number > max:
        max = number
print(max)






