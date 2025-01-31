# secret_number = 9
# guess_count = 0
# guess_limit = 3
# while guess_count < guess_limit:
#     guess = int(input('Guess: '))
#     guess_count += 1
#     if guess == secret_number:
#         print('You Won!!')
#         break
# else:
#     print('Sorry, you did not guess the number')

# msg = input("What is the secret password? ")
# while msg != "bananas":
#     print("Wrong!!")
#     msg = input("What is the secret password? ")
# print("Correct!!")

# num = 1
# while num < 21:
#     print(num)
#     num += 2

# # without string multiplication - ugly
# for num in range(1,11):
#     count = 1
#     smileys = ""
#     while count <= num:
#         smileys += "\U0001f600"
#         count += 1
#     print(smileys)

# For Loop increments 1 thru 10
# for num in range(1,11):
#     print('\U0001f600' * num)

# Nested For Loop - same increment as above, x number of times
# for x in range(4):
#     for num in range(1,11):
#         print('\U0001f600' * num)

# alternative While Loops with for loop
for x in range(4):
    i = 1
    while i <= 10:
        print('\U0001f600' * i)
        i += 1
print('Done')