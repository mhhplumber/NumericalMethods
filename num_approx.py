def main:
	import matplotlib.pyplot as plt

# graphwin: the window to plot on
# func: the function to model
# y: y initial
# t t initial
# h: step size
# res: number of points desired
#
# Uses Euler's method to approximate a function and plot it
def euler(graphwin, func, y, t, h, res):
	if (res):
		graphwin.plot(t, y)
		euler(graphwin, func, y + h * func(t, y), t + h, h, res--)

