import unittest
import requests
import json

URL = f"https://jsonplaceholder.typicode.com"

headers = {"Content-Type": "application/json", "Accept": "application/json"}


class BaseTest(unittest.TestCase):

    def test_get_all_posts(self):
        response = requests.get(URL + "/posts", headers=headers)
        self.assertIn(response.status_code, [200, 404])
        data = response.json()
        assert "qui est esse" in data[1]["title"]
        if response.status_code == 200:
            print("Posts retrieved successfully")
        else:
            print("Unable to retieve posts")

    def test_get_single_post(self):
        task_id = "11"
        response = requests.get(URL + "/posts/" + task_id, headers=headers)
        data = response.json()
        self.assertIn(response.status_code, [200, 404])
        print(response.status_code)
        if response.status_code != 200:
            print("No such post exists")
        else:
            print("Single post retrieved succesfully")

    def test_create_post(self):
        payload = {"userId": "102", "title": "point", "body": "blank"}
        response = requests.post(
            URL + "/posts", data=json.dumps(payload), headers=headers
        )
        self.assertIn(response.status_code, [200, 404, 201])
        print(response.status_code)
        if response.status_code == 404:
            print("No post to update")
        else:
            print("Task created successfully")

    def test_update_post_by_patch(self):
        payload = {"body": "break"}
        response = requests.patch(
            URL + "/posts/102", headers=headers, data=json.dumps(payload)
        )
        print(response.status_code)
        self.assertIn(response.status_code, [200, 404])
        if response.status_code == 200:
            print("Task updated successfully")
        else:
            print("No task updated")


if __name__ == "__main__":
    unittest.main()
