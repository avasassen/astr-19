#import libraries

import numpy as np 
import matplotlib.pyplot as plt 

# define a nice plot
def scatter_plot(x,y,z,zerr,
	flag_save=True,    #save the figure?
	xlabel='x',        #x-axis label
	ylabel='y',        #y-axis label
	lcolor='red',      #line color
	pcolor='gold',     #point color
	fs=14,             #font size
	fname='scatter_plot.png'):  #default plot filename
	
	#by default, flag_save = True, and we'll save the figure
	#to a file. The plot filenae fname = 'plot.png' by
	#default, but we can change this

	#define a figure and axis 
	f, ax = plt.subplots(1,1,figsize=(4,4))

	#plot y vs. x
	ax.plot(x,y,color=lcolor,linewidth=1.5,label='model(line)')  #a line
	ax.errorbar(x,z,yerr=zerr,fmt='o',color=pcolor,markersize=3,label='data (points)')  #circles

	#label our axes
	ax.set_xlabel(xlabel,fontsize=fs)
	ax.set_ylabel(ylabel,fontsize=fs)

	#create a legend without a frame
	#in the upper left hand corner
	ax.legend(loc='upper left', frameon=False)

	#save the plot?
	if(flag_save):
		plt.savefig(fname,bbox_inches='tight',dpi=400)
# define main
def main():
	print('Making a plot...')

	#make a dummy x variable
	x = np.linspace(0,1,10)

	#make a dummy y variable
	y = x**2

	#make a secound dependnt variable
	#equal to y plus gaussian scatter
	#with RMS size of 0.1
	z = y + np.random.normal(scale=0.1,size=len(x))
	zerr = np.full_like(x,0.1)

	#make the plot
	scatter_plot(x,y,z,zerr)

#execute main
if __name__ == '__main__':
	main()