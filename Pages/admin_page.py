from HelperClasses.locators import Locators
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

def loop_check(self, username, listy):
    for person in listy:
        if person == username:
            return True
    return False



class AdminPage():

    def __init__(self, browser):
        #for navigating to admin and sorting table
        self.browser = browser
        self.admin_link_on_dash_id = Locators.admin_link_on_dash_id #to go to admin age on dash
        self.admin_page_employe_xpath = Locators.admin_page_employe_xpath
        self.employee_list = Locators.employee_list
        #for adding new employee
        self.admin_user_type_dropdown_id = Locators.admin_user_type_dropdown_id
        self.employe_name_textbox_id = Locators.employe_name_textbox_id
        self.employee_user_name_id = Locators.employee_user_name_id
        self.employee_status_id = Locators.employee_status_id
        self.employee_password_id = Locators.employee_password_id
        self.employee_password_confirm_id = Locators.employee_password_confirm_id
        self.admin_employee_add_save_btn_id = Locators.admin_employee_add_save_btn_id
        self.add_button_on_admin_page_id = Locators.add_button_on_admin_page_id


    def click_add_on_admin_page(self):
        self.browser.find_element_by_id(self.add_button_on_admin_page_id).click()



    def test_add_new_user(self, username, user_role, employee_name, status, password):
        #self.browser.find_element_by_name(self.admin_user_type_dropdown_id).select_by_visible_text(user_role)
        self.browser.find_element_by_id(self.employe_name_textbox_id).send_keys(employee_name)
        self.browser.find_element_by_id(self.employee_user_name_id).send_keys(username)
        #self.browser.find_element_by_id(self.employee_status_id).select_by_visible_text(status)
        self.browser.find_element_by_id(self.employee_password_id).send_keys(password)
        self.browser.find_element_by_id(self.employee_password_confirm_id).send_keys(password)
        self.browser.find_element_by_id(self.admin_employee_add_save_btn_id).click()

        #checks whether employee column was properly sorted	on admin page

    def set_up_table_xpaths(self):
        listy = []
        table =  self.browser.find_element_by_xpath("//table[@id='resultTable']")

        for row in table.find_elements_by_xpath(".//tr"):
            listy.append( [td.text for td in row.find_elements_by_xpath(".//td[@class='left'][3]") ] ) #
        print(listy)
        listy2 = sorted(listy)
        print(listy2)
        assert(listy2 == listy)


    def click_admin_tab(self): #cannot get this to work consistently so just using get method
        print("TESTING ADMIN TAB FUNCTION CLICK")
        #time.sleep(15)
        #self.browser.find_element_by_id(self.admin_link_on_dash_id).click()  #THIS IS NOT WORKING
        print("testing after click")
        #self.browser.find_element_by_xpath("/html/body/div[1]/div[2]/ul/li[1]/a/b").click()  #for just tesing purposes


        try:
            print("inside try block for admin button")
            wait = WebDriverWait(self.browser, 111)
            element = wait.until(EC.element_to_be_clickable((By.ID, self.admin_link_on_dash_id)))
            element.click()
            #self.browser.find_element_by_link_text("Admin").click()
            #self.browser.get("https://opensource-demo.orangehrmlive.com/index.php/admin/viewSystemUsers")
        except TimeoutError:
            raise Exception("Element not found or not clickable")


    def click_on_employee_name_to_sort(self):
        self.browser.find_element_by_xpath(self.admin_page_employe_xpath).click()



    #loops through employee table and checks if the username added exists in it after the add
    def check_if_add_worked(self, username): ##adding function to make sure added user is now in table
        #time.sleep(15)

        table = self.browser.find_element_by_xpath("//table[@id='resultTable']")
        listy = []
        for row in table.find_elements_by_xpath(".//tr"):
            listy.append([td.text for td in row.find_elements_by_xpath(".//td[@class='left'][1]")])
        assert(loop_check(username, listy))












