import numpy as np     #we use numpy for lots of things

def main():
	i = 0       #integers can be declared with a number
	n = 10      #here is another integer
	x = 19.0    #floating point numbers are declared with a "."

	# we can use numpy to declare arrys quickly

	y = np.zeros(n,dtype=float) #declared 10 zeros as flosts using np

	# we can use for loops to iterate with a variable

	for i in range (n):      #i in range [0,n-1]
		y[i] = 2.0 * float(i) + 1.      #set y = 2i+1 as floats

	#we can also simply iterate through a variable
	for y_element in y:
		print(y_element)

#execute the main funtion
if __name__ == "__main__":
	main()