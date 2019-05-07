
from HelperClasses.locators import Locators
class HomePage():

	def __init__(self,browser):
		self.browser = browser
		
		self.welcome_admin_button_id = Locators.welcome_admin_button_id
		self.logout_link_text = Locators.logout_link_text


	def click_welcome(self):
		self.browser.find_element_by_id(self.welcome_admin_button_id).click()


	def click_logout(self):
		self.browser.find_element_by_link_text(self.logout_link_text).click()


	

