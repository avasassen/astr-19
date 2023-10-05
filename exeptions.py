# python exeptions let you deal with
# unexpectied results

try:
	print(a)    #this will throw an exception since a is not defined
except:
	print("a is not defined!")

# there are specific errors to help with cases
try:
	print(a)    #this will throw an exception since a is not defined
except NameError:
	print("is is still not defined!")
except:
	print("Something else went wrong")

#this will break ut program
#since a is not defined
print(a)