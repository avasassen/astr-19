#define the main function
def main(): 

	#define the filename
	fname = 'test_data.txt'

	#open the file with read mode
	f = open(fname, 'r')

	#print the name of the file
	print(f.name)

	#read the data as a list with an
	#entry for each line
	test_data = f.readlines()

	#close the file
	f.close()

	#print the info from the file
	print(test_data)

#define a statement to run python 
if __name__ == '__main__':
	main()

