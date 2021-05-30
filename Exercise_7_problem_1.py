#!/usr/bin/env python
# coding: utf-8

# ## Problem 1: Simple scatter plot using random 
# 
# We can generate random numbers using using a method `random.rand()` from the [NumPy package](https://numpy.org/). This example generates 10 random values:
# 
# ```
# import numpy as np
# random_numbers = np.random.rand(10)
# 
# ```
# 
# ### Part 1
# 
# Create an new data frame called `data` and add 1000 random numbers (`float`) into a new column `x` and another 1000 random numbers (`float`) into a new column `y`.

import numpy as np
import pandas as pd

# YOUR CODE HERE 1 to set data
# Create a DataFrame, data
data = pd.DataFrame()
# Create data_x with 1000 ramdom value
data_x = np.random.rand(1000)
# Create data_y with 1000 ramdom value
data_y = np.random.rand(1000)

# Set data_x and data_y to the DataFrame, data
data["x"] = data_x
data["y"] = data_y

# Check your random values
print(data.head())

# Check that you have the correct number of rows
assert len(data) == 1000, "There should be 1000 rows of data."


# ### Part 2
# 

# YOUR CODE HERE 2 to set colors
# Create colors with 1000 ramdom value
# It will be used to plot random colors
colors = np.random.rand(1000)

# This test print should print out 10 first numbers in the variable colors
print(colors[0:10])

# Check that the length matches
assert len(colors) == 1000, "There should be 1000 random numbers for colors"


# ### Part 3 
# 
# #### Part 3.1
# 
# Create a scatter plot of points with random colors
# 
# #### Part 3.2
# 
# #### Part 3.3
# 

# Plot a scatter plot
# YOUR CODE HERE 3
# Import matplotlib.pyplot to plot data
import matplotlib.pyplot as plt
# Scatter plot with some options
plt.scatter(data['x'], data['y'], s = 50, c = colors, cmap = 'rainbow', edgecolor = 'black')

# Add labels and title
# YOUR CODE HERE 4
# Create variables which store the text of title, x-label, and y-label
title = 'My random candy points'
xlabel = 'Xlabel'
ylabel = 'Ylabel'

# Add them to the plot
plt.title(title)
plt.xlabel(xlabel)
plt.ylabel(ylabel)

# Save the plot as a png file:
outputfp = "my_first_plot.png"

# YOUR CODE HERE 5
# Save the figure
plt.savefig(outputfp)

# This test print statement should print the output filename of your figure
print("Saved my first plot as:", outputfp)

#Check that the file exists (also go and open the file to check that everything is ok!)
import os

assert os.path.exists(outputfp), "Can't find the output image."


# Remember to commit your changes (including the image file) to your GitHub repo!
# 
# ### Done!
# 
# Now you can move to [problem 2](Exercise-7-problem-2.ipynb).
