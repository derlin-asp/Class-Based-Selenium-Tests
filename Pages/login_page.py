from HelperClasses.locators import Locators

class LoginPage():

	def __init__(self, browser):
		print ("INSIDE INTI CONST")
		self.browser = browser
		self.username_textbox_name = Locators.username_textbox_name
		self.pass_textbox_name = Locators.pass_textbox_name
		self.submit_button_name = Locators.submit_button_name


	def enter_username(self, username):
		print("dsdasda")
		self.browser.find_element_by_name(self.username_textbox_name).clear()
		self.browser.find_element_by_name(self.username_textbox_name).send_keys(username)
	
	def enter_password(self, password):
		self.browser.find_element_by_name(self.pass_textbox_name).clear()
		self.browser.find_element_by_name(self.pass_textbox_name).send_keys(password)


	def click_submit_on_login_page(self):
		self.browser.find_element_by_name(self.submit_button_name).click()





