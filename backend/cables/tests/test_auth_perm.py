from django.test import TestCase

# from django.utils.timezone import datetime
from rest_framework.test import APIClient

# from cables.models import Pole
from commons.tests.tests_commons import createTestUser, logTestUser

# from sinp_nomenclatures.models import Item, Type


class AuthPermTestCase(TestCase):
    """Class to test authentication/permission scheme from Django.

    This test is based on Pole as example. "isAuthenticated" and "DjangoModelPermissions" are used and tested.
    """

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

    # def test_get_with_anonymous_user(self):
    #     resp = self.anonymous_client.get("/api/cables/poles/edit/")
    #     self.assertEquals(resp.status_code, 401)
    #     resp = self.anonymous_client.get("/api/cables/poles/info/")
    #     self.assertEquals(resp.status_code, 401)

    # def test_post_with_anonymous_user(self):
    #     resp = self.anonymous_client.post("/api/cables/poles/edit/", data={})
    #     self.assertEquals(resp.status_code, 401)

    # def test_put_with_anonymous_user(self):
    #     resp = self.anonymous_client.put("/api/cables/poles/edit/", data={})
    #     self.assertEquals(resp.status_code, 401)

    # def test_patch_with_anonymous_user(self):
    #     resp = self.anonymous_client.patch("/api/cables/poles/edit/", data={})
    #     self.assertEquals(resp.status_code, 401)

    # def test_delete_with_anonymous_user(self):
    #     resp = self.anonymous_client.delete("/api/cables/poles/edit/")
    #     self.assertEquals(resp.status_code, 401)

    # def test_get_with_unauthentified_user(self):
    #     resp = self.unauthentified_client.get("/api/cables/poles/edit/")
    #     self.assertEquals(resp.status_code, 401)
    #     resp = self.unauthentified_client.get("/api/cables/poles/info/")
    #     self.assertEquals(resp.status_code, 401)

    # def test_post_with_unauthentified_user(self):
    #     resp = self.unauthentified_client.post(
    #         "/api/cables/poles/edit/", data={}
    #     )
    #     self.assertEquals(resp.status_code, 401)

    # def test_put_with_unauthentified_user(self):
    #     resp = self.unauthentified_client.put(
    #         "/api/cables/poles/edit/", data={}
    #     )
    #     self.assertEquals(resp.status_code, 401)

    # def test_patch_with_unauthentified_user(self):
    #     resp = self.unauthentified_client.patch(
    #         "/api/cables/poles/edit/", data={}
    #     )
    #     self.assertEquals(resp.status_code, 401)

    # def test_delete_with_unauthentified_user(self):
    #     resp = self.unauthentified_client.delete("/api/cables/poles/edit/")
    #     self.assertEquals(resp.status_code, 401)

    # def test_get_with_unauthorized_user(self):
    #     # no restriction for view based on django permission
    #     resp = self.unauthorized_client.get("/api/cables/poles/edit/")
    #     self.assertEquals(resp.status_code, 200)
    #     resp = self.unauthorized_client.get("/api/cables/poles/info/")
    #     self.assertEquals(resp.status_code, 200)

    # def test_post_with_unauthorized_user(self):
    #     resp = self.unauthorized_client.post(
    #         "/api/cables/poles/edit/", data={}
    #     )
    #     self.assertEquals(resp.status_code, 403)

    # def test_put_with_unauthorized_user(self):
    #     resp = self.unauthorized_client.put("/api/cables/poles/edit/", data={})
    #     self.assertEquals(resp.status_code, 403)

    # def test_patch_with_unauthorized_user(self):
    #     resp = self.unauthorized_client.patch(
    #         "/api/cables/poles/edit/", data={}
    #     )
    #     self.assertEquals(resp.status_code, 403)

    # def test_delete_with_unauthorized_user(self):
    #     resp = self.unauthorized_client.delete(
    #         "/api/cables/poles/edit/", data={}
    #     )
    #     self.assertEquals(resp.status_code, 403)

    # def test_all_with_authorized_user(self):
    #     # create owners (nomenclature items) needed to create poles
    #     type = Type.objects.create(
    #         code="code",
    #         mnemonic="owner",
    #         label="owner",
    #         status="VALID",
    #         created_by=self.user,
    #         create_date=datetime.today(),
    #         update_date=datetime.today(),
    #     )
    #     type.save()
    #     owner_pk = []
    #     for i in [1, 2]:
    #         item = Item.objects.create(
    #             type=type,
    #             code=f"owner{i}",
    #             mnemonic=f"owner{i}",
    #             label=f"owner{i}",
    #         )
    #         item.save()
    #         owner_pk.append(item.id)

    #     # create 3 DB entries with owner_pk[0]
    #     for i in range(3):
    #         resp = self.authorized_client.post(
    #             "/api/cables/poles/edit/",
    #             data={
    #                 "type": "Feature",
    #                 "geometry": {
    #                     "type": "Point",
    #                     "coordinates": [0, 0],
    #                 },
    #                 "properties": {
    #                     "owner": owner_pk[0],
    #                 },
    #             },
    #             format="json",
    #         )
    #         self.assertEquals(resp.status_code, 201)

    #     # create 3 DB entries with owner_pk[1]
    #     for i in range(3):
    #         resp = self.authorized_client.post(
    #             "/api/cables/poles/edit/",
    #             data={
    #                 "type": "Feature",
    #                 "geometry": {
    #                     "type": "Point",
    #                     "coordinates": [0, 0],
    #                 },
    #                 "properties": {
    #                     "owner": owner_pk[1],
    #                 },
    #             },
    #             format="json",
    #         )
    #         self.assertEquals(resp.status_code, 201)

    #     # get id of first Pole with owner=owner_pk[0]
    #     first_id = Pole.objects.filter(owner=owner_pk[0])[0].id
    #     # get json data from this Pole
    #     resp = self.authorized_client.get(
    #         f"/api/cables/poles/edit/{first_id}/"
    #     )
    #     data = resp.json()
    #     # change owner value from these data to make put request thereafter
    #     data["properties"]["owner"] = owner_pk[1]
    #     # put request to change the owner
    #     resp = self.authorized_client.put(
    #         f"/api/cables/poles/edit/{first_id}/",
    #         data=data,
    #         format="json",
    #     )
    #     self.assertEquals(resp.status_code, 200)
    #     # change again the owner with patch request
    #     resp = self.authorized_client.patch(
    #         f"/api/cables/poles/edit/{first_id}/", data={"owner": owner_pk[0]}
    #     )
    #     self.assertEquals(resp.status_code, 200)
    #     # test get method on a detail Pole (through edit ViewSet)
    #     resp = self.authorized_client.get(
    #         f"/api/cables/poles/edit/{first_id}/"
    #     )
    #     self.assertEquals(resp.status_code, 200)

    #     # test get method on a list Pole (through edit ViewSet)
    #     resp = self.authorized_client.get("/api/cables/poles/edit/")
    #     self.assertEquals(resp.status_code, 200)

    #     # test get method on a detail Pole (through info ViewSet)
    #     resp = self.authorized_client.get(
    #         f"/api/cables/poles/info/{first_id}/"
    #     )
    #     self.assertEquals(resp.status_code, 200)

    #     # test get method on a list Pole (through info ViewSet)
    #     resp = self.authorized_client.get("/api/cables/poles/info/")
    #     self.assertEquals(resp.status_code, 200)

    #     # test delete method on a detail Pole
    #     resp = self.authorized_client.delete(
    #         f"/api/cables/poles/edit/{first_id}/"
    #     )
    #     self.assertEquals(resp.status_code, 204)

    #     # test get method returns 404
    #     resp = self.authorized_client.get(
    #         f"/api/cables/poles/info/{first_id}/"
    #     )
    #     self.assertEquals(resp.status_code, 404)
