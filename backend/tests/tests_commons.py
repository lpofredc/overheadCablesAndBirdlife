from django.test import TestCase
from rest_framework.test import APIClient

from commons.tests.tests_commons import createTestUser, logTestUser


class Err404TestCase(TestCase):
    def setUp(self):
        self.user = createTestUser("user", "password")
        self.anonymous_client = APIClient()
        self.unauthentified_client = logTestUser("user", "wrong-password")
        self.unauthorized_client = logTestUser("user", "password")
        self.user = createTestUser(
            "user2",
            "password",
            "view_point",
            "add_point",
            "change_point",
            "delete_point",
        )
        self.authorized_client = logTestUser("user2", "password")

    def test_404_for_wrong_uri_anonymous_user(self):
        resp = self.anonymous_client.get("/api/v1/wrong/")
        self.assertEquals(resp.status_code, 404)

    def test_404_for_wrong_uri_unauthentified_user(self):
        resp = self.unauthentified_client.get("/api/v1/wrong/")
        self.assertEquals(resp.status_code, 404)

    def test_404_for_wrong_uri_authorized_user(self):
        resp = self.authorized_client.get("/api/v1/wrong/")
        self.assertEquals(resp.status_code, 404)


# class Err404TestCase(TestCase):
#     """Class to test authentication/permission scheme from Django.

#     This test is based on Pole as example. "isAuthenticated" and "DjangoModelPermissions" are used and tested.
#     """

#     def setUp(self):
#         self.user = createTestUser("user", "password")
#         self.anonymous_client = APIClient()
#         self.unauthentified_client = logTestUser("user", "wrong-password")
#         self.unauthorized_client = logTestUser("user", "password")
#         self.user = createTestUser(
#             "user2",
#             "password",
#             "view_pole",
#             "add_pole",
#             "change_pole",
#             "delete_pole",
#         )
#         self.authorized_client = logTestUser("user2", "password")

#     def test_404_for_wrong_uri_anonymous_user(self):
#         resp = self.anonymous_client.get("/api/v1/wrong/")
#         self.assertEquals(resp.status_code, 404)

#     def test_404_for_wrong_uri_unauthentified_user(self):
#         resp = self.unauthentified_client.get("/api/v1/wrong/")
#         self.assertEquals(resp.status_code, 404)

#     def test_404_for_wrong_uri_unauthentified_user(self):
#         resp = self.authorized_client.get("/api/v1/wrong/")
#         self.assertEquals(resp.status_code, 404)
