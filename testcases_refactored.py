import unittest
import requests
import json
import api_helper
import json_helper


class TestCases(unittest.TestCase):
    """
    Sample class for a "RESTful API testing" workshop that will be a part of Octobertest 2015.
    http://www.octobertest.com.br/

    This uses Test Insane's awesome test REST API for the test scenarios:
    http://apps.testinsane.com/rte/
    """
    def test_get_200(self):
        r = api_helper.get("/status/200")

        msg = "Incorrect status code: %d" % r.status_code
        self.assertEqual(r.status_code, 200, msg)

    def test_get_401(self):
        r = api_helper.get("/status/401")

        msg = "Incorrect status code: %d" % r.status_code
        self.assertEqual(r.status_code, 401, msg)

    def test_post_200(self):
        headers = {
            "content-type": "application/json"
        }
        payload = {
            "id": "1",
            "name": "OctoberTest"
        }
        r = api_helper.post("/status/200", headers, payload)
        r_payload = r.json()

        # verify status code
        msg = "Incorrect status code: %d" % r.status_code
        self.assertEqual(r.status_code, 200, msg)
        # verify response payload
        msg = "Response payload did not match the request payload."
        self.assertTrue(json_helper.compare(payload, r_payload), msg)


if __name__ == "__main__":
    unittest.main()
