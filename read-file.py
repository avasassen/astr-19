# define the main function
def main ():
#define the filename
	fname = 'test_data.txt'

	#open the file with read mode
	f = open(fname,'r')

	#print the name of the file
	print(f.name)

	#read the datat as a string
	test_data = f.read()

	#close the file
	f.close()

	#print the info from the file
	print(test_data)

#statement to execute main
if __name__ == "__main__":
	main()