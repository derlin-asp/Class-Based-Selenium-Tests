
#from HelperClasses.locators import Locators
from selenium import webdriver
import unittest
import HtmlTestRunner
from Pages.login_page import LoginPage
from Pages.admin_page import AdminPage


class AdminTest(unittest.TestCase):

	@classmethod
	def setUpClass(cls):
		print("TESTING 1")
		cls.browser = webdriver.Firefox()
		cls.browser.implicitly_wait(10) #now all browser objects will wait for 10 seconds if not found
		cls.browser.maximize_window()
		cls.browser.get("https://opensource-demo.orangehrmlive.com/")


	def test_employee_sort(self):
		browser = self.browser
		login = LoginPage(browser)  #using class as object for this class HAS A
		login.enter_username("Admin")
		login.enter_password("admin123")

		login.click_submit_on_login_page()
		
		
		admin = AdminPage(browser)
		#time.sleep(5)
		admin.click_admin_tab()
		#time.sleep(5)
		admin.click_on_employee_name_to_sort()
		#time.sleep(5)
		admin.set_up_table_xpaths()
		#time.sleep(5)




	@classmethod
	def tearDownClass(cls):
		cls.browser.close()
		cls.browser.quit()
		print("inside teardown")

if __name__ == '__main__': #so it can be run from CLI easily
	unittest.main(testRunner = HtmlTestRunner.HTMLTestRunner(output="/home/dave/Desktop/autop/TestResults/"))

















