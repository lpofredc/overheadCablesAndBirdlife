from django.test import TestCase
from rest_framework.test import APIClient

# from cables.models import Pole
from commons.tests.tests_commons import createTestUser, logTestUser


class AuthPermTestCase(TestCase):
    """Class to test authentication/permission scheme from Django.

    This test is based on Pole as example. "isAuthenticated" and "DjangoModelPermissions" are used and tested.
    """

    fixtures = ["nomenclatures.json"]
    # From this fixtures, nomenclatures of type "owner" matched to pk 13 or 14 among nomenclature items

    def setUp(self):
        self.user = createTestUser("user", "password")
        self.anonymous_client = APIClient()
        self.unauthentified_client = logTestUser("user", "wrong-password")
        self.unauthorized_client = logTestUser("user", "password")
        self.user = createTestUser(
            "user2",
            "password",
            "view_pole",
            "add_pole",
            "change_pole",
            "delete_pole",
        )
        self.authorized_client = logTestUser("user2", "password")

    def test_get_with_anonymous_user(self):
        resp = self.anonymous_client.get("/api/cables/poles/edit")
        self.assertEquals(resp.status_code, 401)
        resp = self.anonymous_client.get("/api/cables/poles/info")
        self.assertEquals(resp.status_code, 401)

    def test_post_with_anonymous_user(self):
        resp = self.anonymous_client.post("/api/cables/poles/edit", data={})
        self.assertEquals(resp.status_code, 401)

    def test_put_with_anonymous_user(self):
        resp = self.anonymous_client.put("/api/cables/poles/edit", data={})
        self.assertEquals(resp.status_code, 401)

    def test_patch_with_anonymous_user(self):
        resp = self.anonymous_client.patch("/api/cables/poles/edit", data={})
        self.assertEquals(resp.status_code, 401)

    def test_delete_with_anonymous_user(self):
        resp = self.anonymous_client.delete("/api/cables/poles/edit")
        self.assertEquals(resp.status_code, 401)

    def test_get_with_unauthentified_user(self):
        resp = self.unauthentified_client.get("/api/cables/poles/edit")
        self.assertEquals(resp.status_code, 401)
        resp = self.unauthentified_client.get("/api/cables/poles/info")
        self.assertEquals(resp.status_code, 401)

    def test_post_with_unauthentified_user(self):
        resp = self.unauthentified_client.post(
            "/api/cables/poles/edit", data={}
        )
        self.assertEquals(resp.status_code, 401)

    def test_put_with_unauthentified_user(self):
        resp = self.unauthentified_client.put(
            "/api/cables/poles/edit", data={}
        )
        self.assertEquals(resp.status_code, 401)

    def test_patch_with_unauthentified_user(self):
        resp = self.unauthentified_client.patch(
            "/api/cables/poles/edit", data={}
        )
        self.assertEquals(resp.status_code, 401)

    def test_delete_with_unauthentified_user(self):
        resp = self.unauthentified_client.delete("/api/cables/poles/edit")
        self.assertEquals(resp.status_code, 401)

    def test_get_with_unauthorized_user(self):
        # no restriction for view based on django permission
        resp = self.unauthorized_client.get("/api/cables/poles/edit")
        self.assertEquals(resp.status_code, 200)
        resp = self.unauthorized_client.get("/api/cables/poles/info")
        self.assertEquals(resp.status_code, 200)

    def test_post_with_unauthorized_user(self):
        resp = self.unauthorized_client.post("/api/cables/poles/edit", data={})
        self.assertEquals(resp.status_code, 403)

    def test_put_with_unauthorized_user(self):
        resp = self.unauthorized_client.put("/api/cables/poles/edit", data={})
        self.assertEquals(resp.status_code, 403)

    def test_patch_with_unauthorized_user(self):
        resp = self.unauthorized_client.patch(
            "/api/cables/poles/edit", data={}
        )
        self.assertEquals(resp.status_code, 403)

    def test_delete_with_unauthorized_user(self):
        resp = self.unauthorized_client.delete(
            "/api/cables/poles/edit", data={}
        )
        self.assertEquals(resp.status_code, 403)


# TODO Create GeoAreas and SensitiveAreas in addition to Owners before creating Poles
# def test_all_with_authorized_user(self):
#     # create 3 DB entries with owner pk = 13
#     for i in range(3):
#         resp = self.authorized_client.post("/api/cables/poles/", data={"owner": 13})
#         self.assertEquals(resp.status_code, 201)

#     # create 3 DB entries with owner pk = 14
#     for i in range(3):
#         resp = self.authorized_client.post("/api/cables/poles/", data={"owner": 14})
#         self.assertEquals(resp.status_code, 201)

#     first_id = Pole.objects.filter(owner=13)[0].id

#     resp = self.authorized_client.put(
#         f"/api/cables/poles/{first_id}/",
#         data={
#             "id": first_id,
#             "owner": 14,
#             "geo_area": [],
#             "sensitivity_area": [],
#         },
#     )
#     self.assertEquals(resp.status_code, 200)

#     resp = self.authorized_client.patch(f"/api/cables/poles/{first_id}/", data={"owner": 13})
#     self.assertEquals(resp.status_code, 200)

#     resp = self.authorized_client.get(f"/api/cables/poles/{first_id}/")
#     self.assertEquals(resp.status_code, 200)

#     resp = self.authorized_client.get("/api/cables/poles/")
#     self.assertEquals(resp.status_code, 200)

#     resp = self.authorized_client.delete(f"/api/cables/poles/{first_id}/")
#     self.assertEquals(resp.status_code, 204)
