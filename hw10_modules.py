def calc_val(stockVal):
	'''Calculate the value of each stock'''
	val = stockVal[-1] - stockVal[0]
	
	return val

def calc_vDist(stockValue, totValue):
	'''Calculate the value distribution of a group of stocks'''
	vDist = stockValue / totValue
	
	return vDist
