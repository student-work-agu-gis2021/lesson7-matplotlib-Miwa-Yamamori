#!/usr/bin/env python
# coding: utf-8

# ## Problem 2 - Plotting temperatures 
# 
# In this problem we will  plot monthly mean temperatures from the Helsinki-Vantaa airpot for the past 30 years.
# 
# ## Input data
# 
# File `data/helsinki-vantaa.csv` monthly average temperatures from Helsinki Vantaa airport. Column descriptions:
# 
# ### Part 1
# 
# Load the Helsinki temperature data (`data/helsinki-vantaa.csv`)
# 
# - Read the data into variable called `data` using pandas
# - Parse dates from the column `'DATE'` and set the dates as index in the dataframe 

# YOUR CODE HERE 1 to read the data into data and parse dates
# Import pandas to read the csv file
import pandas as pd

# Read with parsing dates and setting it as the index
data = pd.read_csv('data/helsinki-vantaa.csv', parse_dates = ['DATE'], index_col = 'DATE')

# This test print should print first five rows
print(data.head())

# Check the number of rows in the data frame
print(len(data))

# ### Part 2
# 
# Select data for a 30 year period (January 1988 - December 2018)
# 
# - Store the selection in a new variable `selection`

# YOUR CODE HERE 2
# Create selection with selected data for the period
# January 1988 started from 19880101, and December 2018 ended at 20181231
selection = data.loc[(data.index >= '19880101') & (data.index <= '20181231')]

# Check that the data was read in correctly:
selection.head()

# Check how many rows of data you selected:
print("Number of rows:", len(selection))


# ### Part 3
# 
# #### Part 3.1
# 
# Create a line plot that displays the temperatures (`TEMP_C`) for yeach month in the 30 year time period:
#      
# #### Part 3.2
# 
# Save your figure as PNG file called `temp_line_plot.png`.
# 

# YOUR CODE HERE 3
# Import matplotlib.pyplot to plot the data
import matplotlib.pyplot as plt

# Create selec_temp_c which has the data of TEMP_C during the selected period
selec_temp_c = selection['TEMP_C']

# Plot them with some options
ax = selec_temp_c.plot(linestyle = "solid", color = "black", marker = "o", figsize = (14,6), markersize = 3)

# Add the title, x-label, and y-label
ax.set_title('Helsinki-Vantaa Airport')
ax.set_xlabel('Time')
ax.set_ylabel('Tempature(Celsius)')

# Add a grid
ax.grid()

# Set output file name
outputfp = "temp_line_plot.png"

# Save plot as image
# YOUR CODE HERE 4
# Save the figure
plt.savefig(outputfp)
import os

#Check that output file exists (also open the file and check that the plot looks ok!)
os.path.exists(outputfp)


# **REMINDER**: Don't forget to upload your figure and the modified notebook into your personal GitHub repository!
# 
# ### Done!
