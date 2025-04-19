# colors = ["purple", "teal", "magenta", "crimson", "emerald", "chartreause", "red", "orange"]


# numbers = [1,2,3,4,5,6]

# friends = ['ashley', 'matt', 'michael']


# [friend[0].upper() + friend[1:] for friend in friends]
# [friend.capitalize() for friend in friends]

# [num*10 for num in range(1,6)]

# [bool(val) for val in [0, [], '']]

# [str(num) for num in numbers]

# [str(num) + "HELLO" for num in numbers]

# evens = [num for num in numbers if num % 2 == 0]
# odds = [num for num in numbers if num % 2 != 0]

# [num*2 if num % 2 == 0 else num/2 for num in numbers]

# with_vowels = "This is so much fun!"
# ''.join(char for char in with_vowels if char not in "aeiou")

# NESTED LOOPS
nested_list = [[1,2,3],[4,5,6],[7,8,9]]

# nested_list[0][1]
# nested_list[2][2]

# for l in nested_list:
# 	for val in l:
# 		print(val)

coords = [[10.423, 9.123], [37.212, -14.092], [21.367, 32.572]]

# # for loc in coords:
# # 	print (loc)
# [10.423, 9.123]
# [37.212, -14.092]
# [21.367, 32.572]

# # or

# for loc in coords:
# 	for coord in loc:
# 		print (coord)
# 10.423
# 9.123
# 37.212
# -14.092
# 21.367
# 32.572

#or 

# [[print(val) for val in l] for l in nested_list]
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9

# board = [[num for num in range(1,4)] for val in range(1,4)]
# print(board)

# [["X" if num % 2 !=0 else "O" for num in range(1,4)] for val in range(1,4)]

# [["*" for x in range(1,4)] for i in range(1,4)]

# Exercise Answer
# answer = [[num for num in range(0,3)] for val in range(0,3)]
# print(answer)

# another exercise
answer = [[i for i in range(0,10)] for num in range(0,10)]
print(answer)