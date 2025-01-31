numbers = [1, 2, 3, 4, 5, 6, 7, 8]
# Typical looping method
##########
# doubled_numbers = []

# for num in numbers:
# 	doubled_number = num * 2
# 	doubled_numbers.append(doubled_number)
###########

# using list comprehensino
# doubled_numbers = [num * 2 for num in numbers]

# print(f"This is the original list: {numbers}")
# print(f"This is the new list: {doubled_numbers}")

# # Examples
# name = 'nicholas'
# cap_name = [char.upper() for char in name]
# print(cap_name)

# friends = ['ashley', 'matt', 'michael']
# friend = [friend[0].upper() for friend in friends]
# print(friend)

# range = [num * 10 for num in range(1,6)]
# print(range)

# string_list = [str(num) for num in numbers]
# print(string_list)

# calculated = [num * 2 if num % 2 == 0 else num/2 for num in numbers]
# print(calculated)

with_vowels = "This is so much fun, I just can't stand it!"
'' .join(char for char in with_vowels if char not in "aeiou")
[char for char in with_vowels if char not in "aeiou"]
''.join(["cool", "dude", "george"])