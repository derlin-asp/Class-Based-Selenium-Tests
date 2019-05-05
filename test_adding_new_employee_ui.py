



from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import unittest
import HtmlTestRunner
from homePage import HomePage
from login_page import LoginPage
from admin_page import AdminPage
import time

class AddingEmployeeUI(unittest.TestCase):

	@classmethod
	def setUpClass(cls):
		print("TESTING 1")
		cls.browser = webdriver.Chrome("/home/dave/Desktop/autop/chromedriver")
		cls.browser.implicitly_wait(10) #now all browser objects will wait for 10 seconds if not found
		cls.browser.maximize_window()
		cls.browser.get("https://opensource-demo.orangehrmlive.com/")


	def test_adding_new_employee(self):
		browser = self.browser


		login = LoginPage(browser)  #using class as object for this class HAS A
		login.enter_username("Admin")
		login.enter_password("admin123")

		login.click_submit_on_login_page()

		admin = AdminPage(browser)
		admin.click_admin_tab()
		admin.click_add_on_admin_page()
		admin.test_add_new_user("username", "ESS", "Robert Craig", "Enabled", "password")
		time.sleep(5)

	@classmethod
	def tearDownClass(cls):
		cls.browser.close()
		cls.browser.quit()
		print("inside teardown")

if __name__ == '__main__': #so it can be run from CLI easily
	unittest.main(testRunner = HtmlTestRunner.HTMLTestRunner(output="/home/dave/Desktop/autop/TestResults/"))

















