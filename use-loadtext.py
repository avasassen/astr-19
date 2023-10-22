#import libraries
import numpy as np 

# define the main function
def main():

	#define the filename
	fname = 'numpy_data.txt'

	#open the file with numpy loadtxt
	test_data = np.loadtxt(fname)

	#print the info from the file
	print(test_data)

	#print the shape of test_data
	print(test_data.shape)

	#print the data type
	print(type(test_data))

# define an indiom to execute main

if __name__ == '__main__':
	main()