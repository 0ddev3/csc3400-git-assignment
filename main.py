from calcultor import add, subtract, multiply, divide, power, square_root

def main():
	print("------Calculator-------")
	print("Pick an Option")
	print("1. Add")
	print("2. Subtract")
	print("3. Multiply")
	print("4. Divide")
	print("5. Power")
	print("6. Square Root")

	choice = input("Enter your choice (1-6)")

	 if choice == "6":
		 a = int(input("Enter a number: "))
		 print("Result:", square_root(a))
	 else: a = int(input("Enter first number: "))
		 b = int(input("Enter second number: "))
	 if choice == "1":
		 print("Result:", add(a, b))
	 elif choice == "2":
		 print("Result:", subtract(a, b))
	 elif choice == "3":
		 print("Result:", multiply(a, b))
	 elif choice == "4":
		 print("Result:", divide(a, b))
	 elif choice == "5":
		 print("Result:", power(a, b))
	 else:
		 print("Invalid choice")
 if __name__ == "__main__":
	 main()		

