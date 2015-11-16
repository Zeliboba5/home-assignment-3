from decimal import Decimal

def add(*args):
	return Decimal(args[0]) + Decimal(args[1])

def sub(*args):
	return Decimal(args[0]) - Decimal(args[1])

def mul(*args):
	return Decimal(args[0]) * Decimal(args[1])

def div(*args):
	if args[1] == 0:
		raise ValueError("Division by zero")

	return Decimal(args[0]) / Decimal(args[1])

def fact(*args):
	if not isinstance(args[0] , int):
		if not args[0].is_integer():
			raise ValueError("Not whole number in factorial")

	if args[0] < 0:
		raise ValueError("Negative number in factorial")

	if args[0] == 0 or args[0] == 1:
		return 1
	
	return args[0] * fact(args[0] - 1) 

operList = {
	"+": add,
	"-": sub,
	"*": mul,
	"/": div,
	"!": fact
}


