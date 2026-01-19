def add(a,b):
	try:
	  return a + b
	except Exception:
		return "invalid input please try again"

def subtract(a,b):
	try:
	  return a - b
	except Exception:
		return "invalid input please try again"

def multiply(a,b):
	try:
	   return a*b
	except Exception:
	   return "invalid input please try again"

def divide(a,b):
	try:
	  return a/b
	except Exception:
	    return("You cannot divide by zero, please try again")

def power(a,b):
	try:
	  return a**b
	except Exception:
		return "invalid input please try again"

def square_root(a):
    try:
        if a < 0:
            return "You cannot take the square root of a negative number."
        return a ** 0.5
    except Exception:
        return "Invalid input, please try again"

