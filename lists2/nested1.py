
nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

[[print(val) for val in l] for l in nested_list]

for l in nested_list:
	for val in l:
		print(val)

board = [[num for num in range(0,3)] for val in range(1,4)]
print(board)

[["x" if num % 2 != 0 else "o" for num in range(1,4)] for val in range(1,4)]

answer = [[i for i in range(0,10)] for num in range(0,10)]

[["*" for num in range(1,4)] for val in range(1,4)]

