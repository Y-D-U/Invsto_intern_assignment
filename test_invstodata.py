import unittest
import pandas as pd
import numpy


file=r"C:\Users\HP\Downloads\HINDALCO_1D.xlsx"

data=pd.read_excel(file)

def readData(data):
	float_cols=["open","high","low","close"]
	int_cols=["volume"]
	str_cols=["instrument"]
	date_cols=["datetime"]
	for val in float_cols:
		for elem in data[val]:
			if not (isinstance(elem,numpy.float64) or isinstance(elem,float)):
				raise TypeError("Not a float") 
	for val in int_cols:
		if elem in data[val]:
			if not isinstance(elem,numpy.int64) or isinstance(elem,int):
				raise TypeError("Not an int")
	for val in date_cols:
		if elem in data[val]:
			if not (isinstance(elem,pd._libs.tslibs.timestamps.Timestamp)):
				raise TypeError("Not a datetime")


	
class TestData(unittest.TestCase):
	def test_types(self):
		self.assertRaises(TypeError,readData,data)


	