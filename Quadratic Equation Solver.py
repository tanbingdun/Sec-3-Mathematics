while True:

	import math

	print("Welcome to the Quadratic Equation Solver!")
	print("Here, you will solve quadratic eqations of the form ax^2 + bx + c = 0.")

# Invite user for the value of a, b, c and d.
	a = float(input("Enter the coefficient of x^2: "))
	b = float(input("Enter the coefficient of x: "))
	c = float(input("Enter the constant term on the left hand side: "))

# Check the nature of roots.
	discriminant = b * b - 4 * a * c

	if discriminant < 0:
		print ("There are no real roots!\n")
	elif discriminant == 0:
		print (f"The solution of the equation is {-b / (2 * a):.2f}.\n")
	else:
		x1 = (-b + math.sqrt(b*b - 4 * a * c)) / (2 * a)
		x2 = (-b - math.sqrt(b*b - 4 * a * c)) / (2 * a)
		print(f"The solutions are {x1:.2f} and {x2:.2f}.\n")
		
	exit = input('Do you wish to continue? Type "Y" for yes and "N" for no. ').lower()
	
	if exit == "n" or "no":
		break
