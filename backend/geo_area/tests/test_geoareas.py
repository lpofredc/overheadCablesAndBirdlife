from django.contrib.gis.geos import MultiPolygon, Polygon
from django.test import TestCase

# from django.utils.timezone import datetime
from rest_framework.test import APIClient
from sinp_nomenclatures.models import Nomenclature  # , Type# import json

from commons.tests.tests_commons import createTestUser, logTestUser
from geo_area.models import GeoArea


class GeoAreaAnonymousAuthenticationTestCase(TestCase):
    """Class to test authentication/permission scheme for GeoArea and anonymous user.

    Include tests for user trying to log-in with wrong password
    """

    # fixture includes:
    # - at least 2 points, 2 lines, 3 diagnosis, 3 operations, 2 GeoAreas, 2 SensitiveAreas, 2 media
    # (pictures), 2 mortality cases
    # - It contains needed sinp_nomenclature items (stand for dictionanry for specific data)
    fixtures = [
        "commons/tests/fixtures/test_nomenclatures.xml",
        "commons/tests/fixtures/test_geo_area.xml",
    ]

    def setUp(self):
        self.anonymous_client = APIClient()
        # create user trying to log-in with wrong password
        self.user = createTestUser("user", "password")
        self.unauthentified_client = logTestUser("user", "wrong-password")
        # get pk from the first geoarea
        self.pk = GeoArea.objects.all()[0].id

    def test_get_list_with_anonymous_user(self):
        resp = self.anonymous_client.get("/api/v1/geoareas/")
        self.assertEquals(resp.status_code, 401)
        resp = self.unauthentified_client.get("/api/v1/geoareas/")
        self.assertEquals(resp.status_code, 401)

    def test_get_detail_with_anonymous_user(self):
        resp = self.anonymous_client.get(f"/api/v1/geoareas/{self.pk}/")
        self.assertEquals(resp.status_code, 401)
        resp = self.unauthentified_client.get(f"/api/v1/geoareas/{self.pk}/")
        self.assertEquals(resp.status_code, 401)

    def test_create_with_anonymous_user(self):
        resp = self.anonymous_client.post("/api/v1/geoareas/")
        self.assertEquals(resp.status_code, 401)
        resp = self.unauthentified_client.post("/api/v1/geoareas/")
        self.assertEquals(resp.status_code, 401)

    def test_update_with_anonymous_user(self):
        resp = self.anonymous_client.put(f"/api/v1/geoareas/{self.pk}/")
        self.assertEquals(resp.status_code, 401)
        resp = self.unauthentified_client.put(f"/api/v1/geoareas/{self.pk}/")
        self.assertEquals(resp.status_code, 401)

    def test_partial_update_with_anonymous_user(self):
        resp = self.anonymous_client.patch(f"/api/v1/geoareas/{self.pk}/")
        self.assertEquals(resp.status_code, 401)
        resp = self.unauthentified_client.patch(f"/api/v1/geoareas/{self.pk}/")
        self.assertEquals(resp.status_code, 401)

    def test_partial_delete_with_anonymous_user(self):
        resp = self.anonymous_client.delete(f"/api/v1/geoareas/{self.pk}/")
        self.assertEquals(resp.status_code, 401)
        resp = self.unauthentified_client.delete(
            f"/api/v1/geoareas/{self.pk}/"
        )
        self.assertEquals(resp.status_code, 401)


class GeoAreaUnauthorizedAuthenticationTestCase(TestCase):
    """Class to test authentication/permission scheme for Geoarea and unauthorized user."""

    # fixture includes:
    # - at least 2 points, 2 lines, 3 diagnosis, 3 operations, 2 GeoAreas, 2 SensitiveAreas, 2 media
    # (pictures), 2 mortality cases
    # - It contains needed sinp_nomenclature items (stand for dictionanry for specific data)
    fixtures = [
        "commons/tests/fixtures/test_nomenclatures.xml",
        "commons/tests/fixtures/test_geo_area.xml",
    ]

    def setUp(self):
        self.user = createTestUser("user", "password")
        self.unauthorized_client = logTestUser("user", "password")
        # get pk from the first geoarea
        self.pk = GeoArea.objects.all()[0].id

    # no restriction for read only by default with Django
    def test_get_list_with_unauthorized_user(self):
        resp = self.unauthorized_client.get("/api/v1/geoareas/")
        self.assertEquals(resp.status_code, 200)

    # no restriction for read only by default with Django
    def test_get_detail_with_unauthorized_user(self):
        resp = self.unauthorized_client.get(f"/api/v1/geoareas/{self.pk}/")
        self.assertEquals(resp.status_code, 200)

    def test_create_with_unauthorized_user(self):
        resp = self.unauthorized_client.post(f"/api/v1/geoareas/{self.pk}/")
        self.assertEquals(resp.status_code, 403)

    def test_update_with_unauthorized_user(self):
        resp = self.unauthorized_client.put(f"/api/v1/geoareas/{self.pk}/")
        self.assertEquals(resp.status_code, 403)

    def test_partial_update_with_unauthorized_user(self):
        resp = self.unauthorized_client.patch(f"/api/v1/geoareas/{self.pk}/")
        self.assertEquals(resp.status_code, 403)

    def test_partial_delete_with_unauthorized_user(self):
        resp = self.unauthorized_client.delete(f"/api/v1/geoareas/{self.pk}/")
        self.assertEquals(resp.status_code, 403)


class GeoAreaAuthorizedAuthenticationTestCase(TestCase):
    """Class to test get methods for GeoArea"""

    # - It contains needed sinp_nomenclature items (stand for dictionanry for specific data)
    fixtures = ["commons/tests/fixtures/test_nomenclatures.xml"]

    def setUp(self):
        self.anonymous_client = APIClient()
        # create client with authentified user
        self.user = createTestUser("user", "password")
        self.authentified_client = logTestUser("user", "password")

    def test_get_geo_areas(self):
        # get id of a geoarea type in nomanclature (the first one)
        ga_type = (
            Nomenclature.objects.all()
            .filter(type__mnemonic="geoarea_type")[0]
            .id
        )
        # create 2 GeoArea (no request as post method was not implemented: not to be created by
        # users but directly from DB)
        ga = GeoArea.objects.create(
            type_id=ga_type,
            name="Geo Area 1",
            code="GA1",
            geom=MultiPolygon(
                Polygon(((-5, 5), (-5, -5), (5, -5), (5, 5), (-5, 5)))
            ),
        )
        ga.save()
        ga = GeoArea.objects.create(
            type_id=ga_type,
            name="Geo Area 2",
            code="GA2",
            geom=MultiPolygon(
                Polygon(((-1, 1), (-1, -1), (1, -1), (1, 1), (-1, 1)))
            ),
        )
        ga.save()
        # method get tested: get all GeoArea
        resp = self.authentified_client.get("/api/v1/geoareas/")
        self.assertEquals(resp.status_code, 200)
        list = resp.json()
        self.assertEquals(len(list), 2)
        # method get tested: get one specific GeoArea

        existing_id = list["features"][0]["id"]
        resp = self.authentified_client.get(f"/api/v1/geoareas/{existing_id}/")
        # self.assertEquals(resp.status_code, 200)
