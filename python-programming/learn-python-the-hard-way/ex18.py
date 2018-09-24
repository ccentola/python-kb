# this one is like your scripts with argv
def print_two(*args):
	arg1, arg2 = args
	print(f"arg1: {arg1}, arg2: {arg2}")
	
# replace args with variable names
def print_two_again(arg1, arg2):
	print(f"arg1: {arg1}, arg2: {arg2}")

# takes one arg
def print_one(arg1):
	print(f"arg1: {arg1}")
	
# replace args with variable names
def print_none():
	print("I got nothing.")
	
print_two("Carl", "Centola")
print_two_again("Carl", "Centola")
print_one("Carl")
print_none()