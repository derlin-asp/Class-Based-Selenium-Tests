
#from HelperClasses.locators import Locators
from selenium import webdriver
import unittest
import HtmlTestRunner
from Pages.homePage import HomePage
from Pages.login_page import LoginPage
import time

class LoginTest(unittest.TestCase):

	@classmethod
	def setUpClass(cls):
		print("TESTING 1")
		cls.browser = webdriver.Firefox()
		cls.browser.implicitly_wait(10) #now all browser objects will wait for 10 seconds if not found
		cls.browser.maximize_window()
		cls.browser.get("https://opensource-demo.orangehrmlive.com/")


	def test_login(self):
		print("INSIDE TEST LOGIN")
		browser = self.browser

		login = LoginPage(browser)  #using class as object for this class HAS A
		login.enter_username("Admin")
		login.enter_password("admin123")
		login.click_submit_on_login_page()

		home = HomePage(browser)

		home.click_welcome()
		#time.sleep(2)
		home.click_logout()


		
		#time.sleep(100)
		'''
		self.browser.get("https://opensource-demo.orangehrmlive.com/")
		self.browser.find_element_by_name("txtUsername").send_keys("Admin")
		self.browser.find_element_by_name("txtPassword").send_keys("admin123")
		self.browser.find_element_by_name("Submit").click()
		self.browser.find_element_by_id("welcome").click()
		self.browser.find_element_by_link_text("Logout").click()

'''
	@classmethod
	def tearDownClass(cls):
		cls.browser.close()
		cls.browser.quit()
		print("inside teardown")

if __name__ == '__main__': #so it can be run from CLI easily
	unittest.main(testRunner = HtmlTestRunner.HTMLTestRunner(output="/home/dave/Desktop/autop/TestResults/"))

















