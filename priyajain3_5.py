import csv
import sys

class invalidFile(Exception):
	def __init__(self, input_file):
		self.input_file = input_file
	
	def __str__(self, message):
		print 'Invalid file!! Please provide valid file'+message

class CompanyShares():
	def __init__(self, input_file):
		if not input_file:
			raise error("Input file is None")
		self.file_name = input_file
		try:
			self.file = open(input_file)
			self.header = self.file.readline()
			self.list = self.getListOfRows()
			self.mapping_dict = self.create_mapping(header = self.header)
		except Exception as e:
			print "Unable to open file. Reason {0}".format(e)

	#This method creates a dictionary which conatins the data of each company for each month of each year. This dictionary can be used for reporting 		#purpose.
	def FormatData(self):
		_dict = {key : {} for key in self.mapping_dict.keys()} 
		temp = {}
		for item in self.list:
			item_arr = item.strip().split(",")
			year_month = str(item_arr[0])+'_'+item_arr[1]
			for key, value in self.mapping_dict.iteritems():
				_dict[key][year_month] = item_arr[value] 		
		return _dict
			

	#This method find the max price of shares for each company and stores the result in a dict.
	def getMaxShare1(self): 
		max_share = {key : 0 for key in self.mapping_dict.keys()}
		max_share_year = {key : '' for key in self.mapping_dict.keys()}
		for item in self.list:
			item_arr = item.strip().split(",")
			year_month = str(item_arr[0])+'_'+item_arr[1]
			for key, value in self.mapping_dict.iteritems():
				if item_arr[value] > max_share[key]:
					temp = {'period':year_month, 'max_price': item_arr[value]}
					max_share_year[key] = temp  
					max_share[key] = item_arr[value] 
			
		return max_share_year
	
	#This method find the max price of shares for each company and stores the result in a dict. This method uses the csv module.
	def getMaxShare2(self):
		try:
			with open(self.file_name) as f:
				_file = csv.DictReader(f)
				field_names =  set(_file.fieldnames)
				company_name = field_names - {'Year', 'Month'}
				max_price = 0
				max_price_dict = {}
				for row in _file:
					for company, price in row.items():
						if company not in company_name:
							continue
						if max_price_dict.has_key(company):
							 if price > max_price_dict[company]['max_price']:
							
								max_price_dict[company]['max_price'] = price
								max_price_dict[company]['period'] = str(row['Year']+'_'+row['Month'])
						else:
							max_price_dict[company] = {'period':'', 'max_price' : 0}
		except (Exception) as e:
        		print "Error: ", str(e)
        		raise
		return max_price_dict
				
		

	'''This method creates a new file and write the maximum price of the company in that file.
	This method calls the getMaxShare1() of this class.'''
	
	def getReport1(self, file_name):
		max_price_year_dict = self.getMaxShare1()
		_file = open(file_name, 'w')
		for key in max_price_year_dict .keys():		
			_file.write("%s got maximum share price $ %s in %s\n" %(key, max_price_year_dict[key]['max_price'], max_price_year_dict[key]['period']))
		_file.close()

	'''This method creates a new file and write the maximum price of the company in that file. 
	This method calls the getMaxShare2() of this class.'''
	
	def getReport2(self, file_name):
		max_price_year_dict = self.getMaxShare2()
		_file = open(file_name, 'w')
		for key in max_price_year_dict .keys():		
			_file.write("%s got maximum share price $ %s in %s\n" %(key, max_price_year_dict[key]['max_price'], max_price_year_dict[key]['period']))
		_file.close()


	#This method returns the list of strings which are row in the file separated by \n

	def getListOfRows(self):
		return [line for line in self.file]

	#This method returns a dictionary which maps the company name with the corresponding index of the header.	
	
	def create_mapping(self, header=None):
		if not header:
			raise error("Header is blank!!")
		
		header_arr = header.strip().split(',')

		#Loop over the header of the file and create a dict object which maps company name with their index.
		_dict = {str:index for index, str in enumerate(header_arr)}
		_dict.pop('Year')
		_dict.pop('Month')
		return _dict
		
		

if __name__ == "__main__":
	try :
		share = CompanyShares(sys.argv[1])
		share.getReport1("report11.csv") #First implementation : No in-built module is used to produce the desired result.
		share.getReport2("report22.csv") #second implementation : module named 'CSV' is used to produce the desired result.
	except Exception as e:
		print "Error Occured. Reason {0}".format(e)
				
			
					