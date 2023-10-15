# Define F(x)
def f(x):
	return x**3 + 8

# Main function
def main():
	# Define x
	x = 9

	# Define the result
	result = f(x)

	#Print result
	print("f(9)= x**3 + 8 is", result)

	#If result is larger than 27 print YAY
	if result > 27:
		print("YAY!")

# Run the function
if __name__ == '__main__':
	main()
