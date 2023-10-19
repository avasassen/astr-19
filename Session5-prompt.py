import numpy as np      # import numpy

def main():       # define the main function
	x = np.linspace(0.0, 2*np.pi, num=1000)     # use linspace to define a
	# loop range start, finish, #s in between
	sinx = np.sin(x)     # define sin(x)
# make our table layout
	print("  x  |   sin(x)  ")
	print("_________________")
# define what is being printed
	for i in range(1000):
		print(f"{x[i]:3f}|{sinx[i]:3f}")

if __name__ == "__main__":
	main()