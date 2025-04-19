# #offered solution 1

# sounds = ["super", "cali", "fragil", "istic", "expi", "ali", "docious"]
# # Define your code below:
# result = ''
# for s in sounds:
#     result += s.upper()
#     print(result)

# # offered solution 2 (successful)
# sounds = ["super", "cali", "fragil", "istic", "expi", "ali", "docious"]
# # Define your code below:
# result = ''
# for s in sounds:
#     result += s
# result = result.upper()
# print(result)


# # my solution (sort of successful - modified to be successful)
sounds = ["super", "cali", "fragil", "istic", "expi", "ali", "docious"]

# # Define your code below:
# i = 0
# while i < len(sounds):
uppersounds = [element.upper() for element in sounds]
result = "".join(uppersounds)
print(result)
# i += 1