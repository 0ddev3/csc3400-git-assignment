import calculator


# This test file contain 5 test cases for my calculator functions
assert add(2, 3) == 5
assert subtract(10, 4) == 6
assert multiply(19, 3) == 57
assert divide(5, 0) == "Error: division by zero"
assert square_root(-4) == "Error: negative square root"

print("All tests passed!")

