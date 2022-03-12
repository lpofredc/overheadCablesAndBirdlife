from django.test import TestCase
from rest_framework.test import APIClient

from commons.tests.tests_commons import createTestUser, logTestUser


class SensitiveAreaAuthorizedAuthenticationTestCase(TestCase):
    """Class to test sensitive_area module"""

    # - It contains needed sinp_nomenclature items (stand for dictionanry for specific data)
    fixtures = ["commons/tests/fixtures/test_nomenclatures.xml"]

    def setUp(self):
        self.anonymous_client = APIClient()
        # create client with authentified user
        self.user = createTestUser("user", "password", "add_sensitivearea")
        self.authentified_client = logTestUser("user", "password")

    def test_create_and_get_sensitive_area(self):
        # method post tested: create 2 SensitiveArea
        data = {
            "name": "Zone Sensible 1",
            "code": "ZS1",
            "geom": {
                "type": "Polygon",
                "coordinates": [[[0, 5], [0, -5], [5, -5], [5, 5], [0, 5]]],
            },
        }
        resp = self.authentified_client.post(
            "/api/v1/sensitive-areas/", data, format="json"
        )
        self.assertEquals(resp.status_code, 201)
        data = {
            "name": "Zone Sensible 2",
            "code": "ZS2",
            "geom": {
                "type": "Polygon",
                "coordinates": [[[-1, 1], [-1, -1], [0, -1], [0, 1], [-1, 1]]],
            },
        }
        resp = self.authentified_client.post(
            "/api/v1/sensitive-areas/", data, format="json"
        )
        self.assertEquals(resp.status_code, 201)
        # method get tested: get all SensitiveArea
        resp = self.authentified_client.get("/api/v1/sensitive-areas/")
        self.assertEquals(resp.status_code, 200)
        list = resp.json()
        self.assertEquals(len(list), 2)
        # method get tested: get one specific SensitiveArea
        existing_id = list["features"][0]["id"]
        resp = self.authentified_client.get(
            f"/api/v1/sensitive-areas/{existing_id}/"
        )
        self.assertEquals(resp.status_code, 200)
