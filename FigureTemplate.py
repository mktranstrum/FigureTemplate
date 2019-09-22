import numpy as np
import pylab

sqrt = np.sqrt

################################################################################
# Setup figure dimensions and matplotlib parameters
# Parameter names should be self-explanatory
# Sepcify the figure size in inches as it will appear in publication (usually 3.5 in width for two-column)
# Then fontsizes specified below will be scaled appropriately
################################################################################
fig_width = 3.5                         # inches  
golden_mean = (sqrt(5)-1.0)/2.0         # Aesthetic ratio
fig_height = fig_width*golden_mean      # height in inches
dpi = 300.0                             # Convert inch to pt

# Margins are specified as a fraction of axes size.
# May need to adjust (especially left and bottom) to accomodate axes labels/tickmarks
leftmargin = 0.15
bottommargin = 0.2
rightmargin = 0.05
topmargin = 0.1
# These two parameters are used for adjusting spacing between subplots (when used)
wspace = 0.2
hspace = 0.2

fig_size =  [fig_width,fig_height]
params = {'backend': 'ps',
          'axes.labelsize': 10,
          'axes.titlesize': 10,
          'legend.fontsize': 10,
          'xtick.labelsize': 10,
          'ytick.labelsize': 10,
          'text.usetex': True,
          'figure.figsize': fig_size}

pylab.rcParams.update(params)


pylab.figure(1)
pylab.clf()
pylab.axes([leftmargin,
            bottommargin,
            1.0 - rightmargin-leftmargin,
            1.0 - topmargin-bottommargin])

################################################################################
# Insert lines below to load data/create plot
################################################################################

x = np.linspace(0, 1, 100)
pylab.plot(x, x*x)

pylab.xlabel("x-axis")
pylab.xticks([0, 0.25, 0.5, 0.75, 1.0])

pylab.ylabel("y-axis")
pylab.yticks([0., 0.5, 1])

pylab.title(r"$\psi^2$")

# Uncomment this line to adjust spacing/location of subplots
# pylab.subplots_adjust(wspace = wspace, hspace = hspace, right = 1.0 - rightmargin, left = leftmargin, top = 1.0 - topmargin, bottom = bottommargin)

# Display or Save Plot
# If run without any arguments, the figure is displayed in a window
# Alternatively, the first argument specifies the file to which the figure is saved
import sys
if len(sys.argv) > 1:
    pylab.savefig(sys.argv[1], dpi = dpi)
else:
    pylab.show()
