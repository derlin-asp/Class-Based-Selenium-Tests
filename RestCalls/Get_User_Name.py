import requests


class UserAPI:


    def get_user_based_on_id(self, user_index):
        self.response = requests.get('https://reqres.in/api/users/' + str(user_index))
        self.response = self.response.json()
        return self.response["data"]["first_name"] + " " + self.response["data"]["last_name"]







