from locators import Locators

class AdminPage():

	def __init__(self, browser):
		#print ("INSIDE INTI CONST")
		self.browser = browser
		self.admin_link_text_on_dash = Locators.admin_link_text_on_dash
		self.admin_page_employe_text = Locators.admin_page_employe_text
		self.employee_list = Locators.employee_list

	#checks whether employee column was properly sorted	on admin page

	def set_up_table_xpaths(self):
		listy = []
		#temp = self.browser.find_elements_by_xpath(self.employee_list)

		table =  self.browser.find_element_by_xpath("//table[@id='resultTable']")

		for row in table.find_elements_by_xpath(".//tr"):
   			listy.append( [td.text for td in row.find_elements_by_xpath(".//td[@class='left'][3]") ] ) #

   		listy2 = sorted(listy)
   		assert(listy2 == listy)	


	def click_admin_tab(self):
		self.browser.find_element_by_link_text(self.admin_link_text_on_dash).click()



	def click_on_employee_name_to_sort(self):
		self.browser.find_element_by_link_text(self.admin_page_employe_text).click()


	def check_if_sort_worked(self):
		temp = self.browser.find_elements_by_xpath(self.employee_list)
	#print(len(temp))

		#for x in range(len(temp)):
		#	temp = self.browser.find_elements_by_xpath(self.employee_list)
		'''
	
		

 	#need way to find highest entry number
		for number of entries in list 
			format xapth for next one
'''

	




