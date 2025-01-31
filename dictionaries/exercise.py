donations = dict(sam=25.0, lena=88.99, chuck=13.0, linus=99.5, stan=150.0, lisa=50.25, harrison=10.0)
values = donations.values()
total = sum(values)
print(total)

# or

total_donations = 0

for donation in donations.values():
	total_donations += donation
print(total_donations)

# or

total_donations = sum(donation for donation in donations.values())

# or

total_donations = sum(donations.values())

for key in donations:
	print(key, "-->", donations[key])