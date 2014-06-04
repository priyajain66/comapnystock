#This is a test file which unit test the method getMaxShare1 and getMaxShare2 of the module priyajain3_5.

#To run this file we need priyajain3_5.py to be present at the same location.

import unittest
import sys
from priyajain3_5 import CompanyShares, invalidFile

class TestCompanySharePrice(unittest.TestCase):
	"""This class class test all 
	the method of priyajain3_5.py """

	def setUp(self):
		self.expected_output = {'Company-A' : {'max_price' : 969, 'period' : '1990_Aug'},\
		 			'Company-B' : {'max_price' : 914, 'period' : '1990_Apr'},\
					'Company-C' : {'max_price' : 917, 'period' : '1991_Feb'},
					'Company-D' : {'max_price' : 971, 'period' : '1991_Apr'},\
					'Company-E' : {'max_price' : 870, 'period' : '1990_Jul'}}
		
		self.file = open('C:\\Users\\Om\\Desktop\\correct.csv')
		
		self.share_correct_file = CompanyShares('C:\\Users\\Om\\Desktop\\correct.csv')
		
		self.expected_mapping_dict = {'Company-A':2, 'Company-B':3, 'Company-C':4, 'Company-D':5, 'Company-E':6}


	def tearDown(self):
		self.file.close()

	def test_get_max_share_1(self):
		actual_output = self.share_correct_file.getMaxShare1()
		for key in self.expected_output.keys():
			self.assertEqual(self.expected_output[key]['period'].upper(), actual_output[key]['period'].upper())
			self.assertEqual(str(self.expected_output[key]['max_price']), str(actual_output[key]['max_price']))

	def test_get_max_share_2(self):
		actual_output = self.share_correct_file.getMaxShare2()
		for key in self.expected_output.keys():
			self.assertEqual(self.expected_output[key]['period'].upper(), actual_output[key]['period'].upper())
			self.assertEqual(str(self.expected_output[key]['max_price']), str(actual_output[key]['max_price']))
	
	def test_create_mapping_dict(self):
		actual_output = self.share_correct_file.create_mapping(self.file.readline())
		for key in self.expected_mapping_dict.keys():
			self.assertEqual(self.expected_mapping_dict[key], actual_output[key])


if __name__ == "__main__":
	suite = unittest.TestLoader().loadTestsFromTestCase(TestCompanySharePrice)
    	unittest.TextTestRunner(verbosity=2).run(suite)            
   	sys.exit()