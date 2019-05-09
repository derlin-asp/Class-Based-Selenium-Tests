import requests

from HelperClasses.locators import Locators

#should prob make a Locators type class for API's
class UserAPI:

    def __init__(self):
        self.payload = {}
        self.response = ""


    def get_user_based_on_id(self, user_index):



        self.response = requests.get('https://reqres.in/api/users/' + str(user_index))
        self.response = self.response.json()



        #print(self.response)
        return self.response["data"]["first_name"] + " " + self.response["data"]["last_name"]



    def register_new_user_using_pass_email(self): #should take inputs for the payload --mabye not the url though
        self.response = requests.post(Locators.register_url_end_point, data=Locators.registration_payload)
        self.response = self.response.json()
        return self.response['id']



#API = UserAPI()

#print (API.get_user_based_on_id() )







