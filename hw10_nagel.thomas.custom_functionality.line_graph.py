"""
Thomas Nagel June 5, 2019
Programming Assignment 10: Adding Custom Functionality - Line Graph

This assignment extends my assignment from week 8, which:
	- Reads information from a JSON file
	- Organizes the data into lists and extracts certain data from the lists
	- Creates a graph and plots the extracted data on the graph
	- Uses exceptions and error handling to print messages to users explaining what went wrong.
To extend that funcionality, this assigment also shows the differences between the daily high and low prices of each stock
"""

#Import functions from module and libraries
from matplotlib import pyplot as plt
import json
from datetime import datetime

#Open JSON file and load data
stocks = 'AllStocks.json'
with open(stocks) as s:
	stock_data = json.load(s)

#Create empty lists for each stock's highs and lows and the dates
AIG_LPrices, AIG_HPrices = [], []
MS_LPrices, MS_HPrices = [], []
FB_LPrices, FB_HPrices = [], []
dates = []

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
		date = datetime.strptime(sDate, '%d-%b-%y')
		if date not in dates:
			dates.append(date)
		
		if sSymbol == 'AIG':
			AIG_LPrice = float(sLow)
			AIG_LPrices.append(AIG_LPrice)
			
			AIG_HPrice = float(sHigh)
			AIG_HPrices.append(AIG_HPrice)
			
		elif sSymbol == 'MSFT':
			MS_LPrice = float(sLow)
			MS_LPrices.append(MS_LPrice)
			
			MS_HPrice = float(sHigh)
			MS_HPrices.append(MS_HPrice)
		
		elif sSymbol == 'FB':
			FB_LPrice = float(sLow)
			FB_LPrices.append(FB_LPrice)
			
			FB_HPrice = float(sHigh)
			FB_HPrices.append(FB_HPrice)

#Print error message if data is missing in any of the lines
except ValueError:
	print('There must have been an error reading the data and adding to the lists.')

#Create a graph of the selected data
try:
	#Plot data
	fig = plt.figure(figsize =(10, 6))
	
	#Plot AIG data
	plt.plot(dates, AIG_LPrices, c = 'orange', label='AIG Lows')
	plt.plot(dates, AIG_HPrices, c = 'red', label='AIG Highs')
	plt.fill_between(dates, AIG_LPrices, AIG_HPrices, facecolor='maroon', alpha=0.1)
	
	#Plot MSFT data
	plt.plot(dates, MS_LPrices, c = 'green', label='MSFT Lows')
	plt.plot(dates, MS_HPrices, c = 'blue', label='MSFT Highs')
	plt.fill_between(dates, MS_LPrices, MS_HPrices, facecolor='aquamarine', alpha=0.1)
	
	#Plot FB data
	plt.plot(dates, FB_LPrices, c = 'turquoise', label='FB Lows')
	plt.plot(dates, FB_HPrices, c = 'purple', label='FB Highs')
	plt.fill_between(dates, FB_LPrices, FB_HPrices, facecolor='blue', alpha=0.1)
	
	#Format plot
	plt.title('Low and High Prices For Stocks Over Time', fontsize=24)
	plt.xlabel('Date (Year-Month)', fontsize=16)
	fig.autofmt_xdate()
	plt.ylabel('Price ($)', fontsize=16)
	plt.tick_params(axis='both', which='major', labelsize=12)
	plt.legend()
	
	#Display plot
	plt.show()

#Print error message if there is an OS Error
except OSError:
	print('There was an error creating the graph.')
