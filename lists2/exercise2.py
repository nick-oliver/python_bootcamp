# answer = [val for val in [1,2,3,4] if val in [3,4,5,6,]]

# answer2 = [val[::-1].lower() for val in ["Elie", "Tim", "Matt"]]
# print(answer2)

answer = []
for x in [1,2,3,4]:
    if x in [3,4,5,6]:
        answer.append(x)
print(answer)
#
answer2 = []
for name in ["Elie", "Tim", "Matt"]:
    answer2.append(name[::-1].lower())
print(answer2)

numbers = [1, 2, 3, 4, 5, 6]
answer2 = [num for num in [1, 2, 3, 4, 5, 6] if num %2 == 0]
print(answer2)


names = ["Oliver", "Gentry", "Pulaski"]
[name[0].upper() for name in names]


answer = [ans for ans in "amazing" if ans not in "aeiou"]