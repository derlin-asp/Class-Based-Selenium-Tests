
#all locators are named with style of:  description_locatortype : id class name etc

class Locators():
	#login page
	username_textbox_name = "txtUsername"
	pass_textbox_name = "txtPassword"
	submit_button_name = "Submit"


	#home page
	welcome_admin_button_id = "welcome"
	logout_link_text = "Logout"

	#admin page 
	admin_link_text_on_dash = "Admin"
	admin_page_employe_text = "Employee Name"

		#employee admin table
	employee_list = "/html/body/div[1]/div[3]/div[2]/div/div/form/div[4]/table/tbody/tr" #/html/body/div[1]/div[3]/div[2]/div/div/form/div[4]/table/tbody/tr[2]/td[4]
						#/html/body/div[1]/div[3]/div[2]/div/div/form/div[4]/table/tbody/tr[3]/td[4]

		#admin user creation					
	admin_user_type_dropdown_id = "systemUser[userType]"					
	employe_name_textbox_id = "systemUser_employeeName_empName"
	employee_user_name_id = "systemUser_userName"
	employee_status_id = "systemUser_status"
	employee_password_id = "systemUser_password"
	employee_password_confirm_id = "systemUser_confirmPassword"

	admin_employee_add_save_btn_id = "btnSave"



	#TimePage
	dash_time_button_id = "menu_time_viewTimeModule"





