
{num: num **2 for num in [1,2,3,4,5,675]}

str1 = 'ABC'
str2 = '123'
combo = {str1[i]: str2[i] for i in range (0, len(str1))}
print (combo)


instructor = {
	'name': 'colt',
	'city': 'dallas',
	'color': 'green'
}

yelling_instructor = {k.upper():v.upper() for k,v in instructor.items()}
print(yelling_instructor)

# conditional logic with dictionaries
num_list = [1,2,3,4,5,6,7,8,9,]
{ num: ("even" if num % 2 == 0 else "odd") for num in num_list }
# or (not using num_list at all, using provided range)
{ num: ("even" if num % 2 == 0 else "odd") for num in range(1,100) }
# or capitalizing specific elements
yelling_instructor = {(k.upper() if k is 'color' else k):v.upper() for k,v in instructor.items()}
print(yelling_instructor)