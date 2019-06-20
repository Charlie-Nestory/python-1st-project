weight=int(input("Enter the Weight value (kg): "))

if weight<=2:
	cost=125
	print("Amount to be paid: R",cost)
else:
	cost=(weight-2)*55+125
	print("Amount to be paid: R",cost)
