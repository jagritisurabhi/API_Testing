import requests
import unittest
from pprint import pprint


class BaseTest(unittest.TestCase):
    base_url = f"https://reqres.in/api"
    per_page_limit = 6
    new_page_per_limit = 4

    def tearDown(self):
        requests.post(self.base_url, data={})

    def test_get_users_by_default_page_limit(self):
        response = requests.get(self.base_url + "/users")
        data = response.json()
        if len(data.keys()) == self.per_page_limit:  # Default limit is 6
            print(f"Default page limit is {self.per_page_limit}")

    def test_custom_pagination(self):
        response = requests.get(self.base_url + "/users?page=1&per_page=4")
        pprint(response.json())
        print(len(response.json().keys()))
        # if len(data.keys()) == self.new_page_per_limit:  # Default limit is 6
        #     print(f"New page limit is {self.new_page_per_limit}")


if __name__ == "__main__":
    unittest.main()
