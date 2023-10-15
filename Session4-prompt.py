# define a class with an initialize
# set of parameters

#import sys
import sys

class Cody:

	# a class for Cody, My favorite animal

	def print(self):
		print("Cody my mini goldndoodle is my favorite animal!")
		print(f"Length of Arms = {self.len_arms}")
		print(f"Length of Legs = {self.len_legs}")
		print(f"Number of eyes = {self.num_eyes}")

		Tail = 'Cody has a tail'
		print(Tail, ':', bool(Tail))

		Furry = 'Cody is furry'
		print(Furry,':', bool(Furry))


	def __init__(self,larms=3,llegs=1,neyes=5.):
		self.len_arms   = larms
		self.len_legs   = llegs
		self.num_eyes   = neyes

def main():

	# set default size of legs
	# and arms
	# and number of eyes
	larms = 9.5
	llegs = 14.5
	neyes = 2

	
	#initialize our cody
	our_cody = Cody(larms=larms,llegs=llegs,neyes=neyes)

	#print our infomation about
	#our cody
	our_cody.print()

#run the program
if __name__ == "__main__":
	main()