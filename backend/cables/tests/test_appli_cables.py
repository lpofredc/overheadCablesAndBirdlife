from django.contrib.gis.geos import Polygon
from django.test import TestCase
from rest_framework.test import APIClient
from sinp_nomenclatures.models import Item

from commons.tests.tests_commons import createTestUser, logTestUser
from geo_area.models import GeoArea


class CreateDiagnosticTestCase(TestCase):
    """Class to test creation of SensitiveArea, Point

    Require creation and consultation of various elements
    """

    # - It contains needed sinp_nomenclature items (stand for dictionanry for specific data)
    fixtures = ["test_nomenclatures.xml"]

    def setUp(self):
        self.anonymous_client = APIClient()
        # create client with authentified user
        self.user = createTestUser(
            "user", "password", "add_sensitivearea", "add_point"
        )
        self.authentified_client = logTestUser("user", "password")

    def test_create_and_get_point(self):
        # CREATE 2 SENSITIVE_AREA
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
        data = {
            "name": "Zone Sensible 2",
            "code": "ZS2",
            "geom": {
                "type": "Polygon",
                "coordinates": [[[-1, 1], [-1, -1], [1, -1], [1, 1], [-1, 1]]],
            },
        }
        resp = self.authentified_client.post(
            "/api/v1/sensitive-areas/", data, format="json"
        )

        # CREATE 2 GEO_AREA
        # get id of a geoarea type in nomanclature (the first one)
        ga_type = (
            Item.objects.all().filter(type__mnemonic="geoarea_type")[0].id
        )
        # create 2 GeoArea (no request as post method was not implemented: not to be created by
        # users but directly from DB)
        ga = GeoArea.objects.create(
            type_id=ga_type,
            name="Geo Area 1",
            code="GA1",
            geom=Polygon(((-5, 5), (-5, -5), (5, -5), (5, 5), (-5, 5))),
        )
        ga.save()
        ga = GeoArea.objects.create(
            type_id=ga_type,
            name="Geo Area 2",
            code="GA2",
            geom=Polygon(((-1, 1), (-1, -1), (1, -1), (1, 1), (-1, 1))),
        )
        ga.save()

        # TEST POINT
        # Create 4 Points:
        # - one inside both SensitiveArea and both GeoArea
        data = {
            "owner_id": 1,
            "geom": {"type": "Point", "coordinates": [0.5, 0.5]},
        }
        resp = self.authentified_client.post(
            "/api/v1/cables/points/", data, format="json"
        )
        self.assertEquals(resp.status_code, 201)
        # method get tested: get one specific Point
        points = resp.json()
        id = points["properties"]["id"]
        resp = self.authentified_client.get(f"/api/v1/cables/points/{id}/")
        self.assertEquals(resp.status_code, 200)
        point = resp.json()
        self.assertEquals(
            len(point["properties"]["sensitive_area"]["features"]), 2
        )
        self.assertEquals(len(point["properties"]["geo_area"]["features"]), 2)

        # - one outside one SensitiveArea and inside both GeoArea
        data = {
            "owner_id": 1,
            "geom": {"type": "Point", "coordinates": [-0.5, 0.5]},
        }
        resp = self.authentified_client.post(
            "/api/v1/cables/points/", data, format="json"
        )
        self.assertEquals(resp.status_code, 201)
        # method get tested: get one specific Point
        points = resp.json()
        id = points["properties"]["id"]
        resp = self.authentified_client.get(f"/api/v1/cables/points/{id}/")
        self.assertEquals(resp.status_code, 200)
        point = resp.json()
        self.assertEquals(
            len(point["properties"]["sensitive_area"]["features"]), 1
        )
        self.assertEquals(len(point["properties"]["geo_area"]["features"]), 2)

        # - one outside both SensitiveArea and both GeoArea
        data = {
            "owner_id": 1,
            "geom": {"type": "Point", "coordinates": [10, 10]},
        }
        resp = self.authentified_client.post(
            "/api/v1/cables/points/", data, format="json"
        )
        self.assertEquals(resp.status_code, 201)
        # method get tested: get one specific Point
        points = resp.json()
        id = points["properties"]["id"]
        resp = self.authentified_client.get(f"/api/v1/cables/points/{id}/")
        self.assertEquals(resp.status_code, 200)
        point = resp.json()
        self.assertEquals(
            len(point["properties"]["sensitive_area"]["features"]), 0
        )
        self.assertEquals(len(point["properties"]["geo_area"]["features"]), 0)

        # same test with values at the limit:
        # => inside one SensitiveArea and one GeoArea
        data = {
            "owner_id": 1,
            "geom": {"type": "Point", "coordinates": [5, 5]},
        }
        resp = self.authentified_client.post(
            "/api/v1/cables/points/", data, format="json"
        )
        self.assertEquals(resp.status_code, 201)
        # method get tested: get one specific Point
        points = resp.json()
        id = points["properties"]["id"]
        resp = self.authentified_client.get(f"/api/v1/cables/points/{id}/")
        self.assertEquals(resp.status_code, 200)
        point = resp.json()
        self.assertEquals(
            len(point["properties"]["sensitive_area"]["features"]), 1
        )
        self.assertEquals(len(point["properties"]["geo_area"]["features"]), 1)

        # test get list
        resp = self.authentified_client.get("/api/v1/cables/points/")
        self.assertEquals(resp.status_code, 200)
        points = resp.json()
        self.assertEquals(len(points["features"]), 4)
