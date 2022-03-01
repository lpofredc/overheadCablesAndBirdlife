from django.test import TestCase

# from django.utils.timezone import datetime
from rest_framework.test import APIClient

from commons.tests.tests_commons import createTestUser, logTestUser
from geo_area.models import GeoArea

# from sinp_nomenclatures.models import Item, Type


class GeoAreaAnonymousAuthenticationTestCase(TestCase):
    """Class to test authentication/permission scheme for GeoArea and anonymous user.

    Include tests for user trying to log-in with wrong password
    """

    # fixture includes:
    # - at least 2 points, 2 lines, 3 diagnosis, 3 operations, 2 GeoAreas, 2 SensitiveAreas, 2 media
    # (pictures), 2 mortality cases
    # - It contains needed sinp_nomenclature items (stand for dictionanry for specific data)
    fixtures = ["test_nomenclatures.xml", "test_geo_area.xml"]

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
    fixtures = ["test_nomenclatures.xml", "test_geo_area.xml"]

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
