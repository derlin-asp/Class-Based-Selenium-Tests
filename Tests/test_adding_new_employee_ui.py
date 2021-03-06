
#from HelperClasses.locators import Locators
import time
import unittest

import HtmlTestRunner
from faker import Faker
from selenium import webdriver

from Pages.admin_page import AdminPage
from Pages.login_page import LoginPage
from RestCalls.Get_User_Name import UserAPI


class AddingEmployeeUI(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("TESTING 1")
        #cls.browser = webdriver.Firefox(executable_path= Locators.Driver_Location)
        cls.browser = webdriver.Firefox()
        cls.browser.implicitly_wait(22) #now all browser objects will wait for 10 seconds if not found
        cls.browser.maximize_window()
        cls.browser.get("https://opensource-demo.orangehrmlive.com/")


    def test_adding_new_employee(self):
        browser = self.browser
        #time.sleep(10)

        login = LoginPage(browser)  #using class as object for this class HAS A
        login.enter_username("Admin")
        login.enter_password("admin123")

        login.click_submit_on_login_page()

        admin = AdminPage(browser)
        admin.click_admin_tab()  # not working
        admin.click_add_on_admin_page()

        fake = Faker()

        #temp_name =  fake.name()


        API = UserAPI()

        print(API.get_user_based_on_id(2))

        temp_id = API.register_new_user_using_pass_email()

        temp_name = API.get_user_based_on_id(temp_id)

        print(temp_name)
        admin.test_add_new_user( temp_name, "ESS", "Robert Craig", "Enabled", "password") #mabye add a way to dynamically get an existing user at random
        admin.check_if_add_worked(temp_name)
        time.sleep(5)

    @classmethod
    def tearDownClass(cls):
        cls.browser.close()
        cls.browser.quit()
        print("inside teardown")

if __name__ == '__main__': #so it can be run from CLI easily
    unittest.main(testRunner = HtmlTestRunner.HTMLTestRunner(output="/home/dave/Desktop/autop/TestResults/"))

















