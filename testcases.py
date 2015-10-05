import unittest
import requests
import json


class TestCases(unittest.TestCase):
    """
    Sample class for a "RESTful API testing" workshop that will be a part of Octobertest 2015.
    http://www.octobertest.com.br/

    This uses Test Insane's awesome test REST API for the test scenarios:
    http://apps.testinsane.com/rte/
    """
    def test_get_200(self):
        uri = "http://apps.testinsane.com/rte/status/200"
        r = requests.get(uri)

        msg = "Incorrect status code: %d" % r.status_code
        self.assertEqual(r.status_code, 200, msg)

    def test_get_401(self):
        uri = "http://apps.testinsane.com/rte/status/401"
        r = requests.get(uri)

        msg = "Incorrect status code: %d" % r.status_code
        self.assertEqual(r.status_code, 401, msg)

    def test_post_200(self):
        uri = "http://apps.testinsane.com/rte/status/200"
        headers = {
            "content-type": "application/json"
        }
        payload = {
            "id": "1",
            "name": "OctoberTest"
        }
        r = requests.post(uri, data=json.dumps(payload), headers=headers)
        r_payload = r.json()

        # verify status code
        msg = "Incorrect status code: %d" % r.status_code
        self.assertEqual(r.status_code, 200, msg)
        # verify "id" key
        msg = "Incorrect id: %s" % r_payload.get("id")
        self.assertEqual(r_payload.get("id"), payload.get("id"), msg)
        # verify "name" key
        msg = "Incorrect name: %s" % r_payload.get("name")
        self.assertEqual(r_payload.get("name"), "payload.get("name")", msg)


if __name__ == "__main__":
    unittest.main()
