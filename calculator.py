from operations import operList

allowedOperations = ["+", "-", "*", "/", "!"]

def calculate(operation, *args):
	if operation not in allowedOperations:
		raise ValueError("Wrong operation")

	func = operList[operation]
	
	return func(*args)
	