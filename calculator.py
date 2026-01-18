def add(a,b):
return a + b

def subtract(a,b):
return a - b

def multiply(a,b):
return a*b

def divide(a,b):
if b == 0:
	raise ValueError("You cannot divide by zero")
return a/b

def power(a,b):
	return a**b

def square_root(a):
if a < 0:
	raise ValueError("You cannot take the square root of a negatibe number.")
	return a ** 0.5
