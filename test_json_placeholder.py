import unittest
import requests
import json

URL = f"https://jsonplaceholder.typicode.com"

headers = {"Content-Type": "application/json", "Accept": "application/json"}


class BaseTest(unittest.TestCase):

    def tearDown(self):
        requests.post(URL, data={})

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
        task_id = "1"
        response = requests.get(URL + "/posts/" + task_id, headers=headers)
        data = response.json()
        self.assertIn(response.status_code, [200, 404])
        print(response.status_code)
        if response.status_code != 200:
            print("No such post exists")
        else:
            print("Requested post retrieved succesfully")

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
            print("Post created successfully")

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

    def test_update_post_by_put(self):
        payload = {"userId": "2", "title": "new input", "body": "new input"}
        response = requests.put(
            URL + "/posts/2", data=json.dumps(payload), headers=headers
        )
        self.assertIn(response.status_code, [200, 201, 404])
        data = response.json()
        assert data["title"] == "new input"
        self.assertEqual(data["title"], "new input")

    def test_remove_post_by_delete(self):
        task_id = "3"
        del_response = requests.delete(URL + "/posts/" + task_id)
        self.assertIn(del_response.status_code, [200, 404])
        if del_response.status_code == 200:
            assert requests.get(URL + "/tasks" + task_id) != 200
            print("Task deleted successfully")
        else:
            print("No task found to delete")


if __name__ == "__main__":
    unittest.main()
