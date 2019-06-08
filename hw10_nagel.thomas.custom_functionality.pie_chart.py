"""
Thomas Nagel June 5, 2019
Programming Assignment 10: Adding Custom Functionality - Pie Chart

This assignment extends my assignment from week 8, which:
	- Reads information from a JSON file
	- Organizes the data into lists and extracts certain data from the lists
	- Creates a graph and plots the extracted data on the graph
	- Uses exceptions and error handling to print messages to users explaining what went wrong.
To extend that funcionality, this assigment also calculates the value distribution of the stocks and plots it in a pie chart instead of a line graph
"""

#Import functions from module and libraries
from matplotlib import pyplot as plt
import json
from datetime import datetime
from hw10_modules import *

#Open JSON file and load data
stocks = 'AllStocks.json'
with open(stocks) as s:
	stock_data = json.load(s)

#Create empty lists to store each stock's values
AIGVal = []
MSVal = []
FBVal = []

#Extract data from JSON file and try to append it to the lists for each stock
try:
	for line in stock_data:
		#Define variables for the attributes from the JSON file
		sSymbol = line['Symbol']
		sDate = line['Date']
		sOpen = line['Open']
		sHigh = line['High']
		sLow = line['Low']
		sClose = line['Close']
		sVolume = line['Volume']
		
		#Append data to the lists
		if sSymbol == 'AIG':
			AIGVal.append(sClose)
			
		elif sSymbol == 'MSFT':
			MSVal.append(sClose)
		
		elif sSymbol == 'FB':
			FBVal.append(sClose)

#Print error message if data is missing or incorrectly formatted in any of the lines
except ValueError:
	print('There must have been an error reading the data and adding to the lists.')

#Calculate value distribution of each stock using functions
try:
	#Calculate each stocks value
	AIG = calc_val(AIGVal)
	MS = calc_val(MSVal)
	FB = calc_val(FBVal)
	
	#Calculate the total value of the stocks
	totVal = AIG + MS + FB
	
	#Calculate the value distribution of each stock based on the total value
	AIG = calc_vDist(AIG , totVal)
	MS = calc_vDist(MS , totVal)
	FB = calc_vDist(FB , totVal)
	
	'''
	print('AIG: ' + str(AIG) + '\n' +
		'MSFT: ' + str(MS) + '\n' +
		'FB: ' + str(FB) + '\n')
	'''

#Print error message if the data in the functions do not work
except ValueError:
	print('There was an error calculating the value distributions of the stocks.')

#Create a pie chart of the selected data
try:
	#Format plot
	fig = plt.figure(figsize =(10, 6))
	labels = 'AIG', 'MSFT', 'FB'
	sizes = [AIG, MS, FB]
	colors = ['red', 'lightgreen', 'lightblue', ]
	
	#Plot data
	plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True, startangle=140)
	plt.title('Value Distribution of Stocks', fontsize=24)
	plt.axis('equal')
	
	#Display plot
	plt.show()
		
#Print error message if there is an OS Error
except OSError:
	print('There was an error creating the graph.')
