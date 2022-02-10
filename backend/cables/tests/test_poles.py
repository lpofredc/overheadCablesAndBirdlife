from django.test import TestCase

# from django.utils.timezone import datetime
from rest_framework.test import APIClient

from cables.models import Pole
from commons.tests.tests_commons import createTestUser, logTestUser

# from sinp_nomenclatures.models import Item, Type


class PoleAnonymousAuthenticationTestCase(TestCase):
    """Class to test authentication/permission scheme for Pole and anonymous user.

    Include tests for user trying to log-in with wrong password
    """

    # fixture includes:
    # - at least 2 poles, 2 segments, 3 visits, 3 operations, 2 GeoAreas, 2 SensitiveAreas, 2 media
    # (pictures), 2 mortality cases
    # - It contains needed sinp_nomenclature items (stand for dictionanry for specific data)
    fixtures = ["test_nomenclatures.xml"]

    def setUp(self):
        self.anonymous_client = APIClient()
        # create user trying to log-in with wrong password
        self.user = createTestUser("user", "password")
        self.unauthentified_client = logTestUser("user", "wrong-password")
        # get pk from the first Segment
        self.pk = Pole.objects.all()[0].id

    def test_get_list_with_anonymous_user(self):
        resp = self.anonymous_client.get("/api/v1/cables/poles/")
        self.assertEquals(resp.status_code, 401)
        resp = self.unauthentified_client.get("/api/v1/cables/poles/")
        self.assertEquals(resp.status_code, 401)

    def test_get_detail_with_anonymous_user(self):
        resp = self.anonymous_client.get(f"/api/v1/cables/poles/{self.pk}/")
        self.assertEquals(resp.status_code, 401)
        resp = self.unauthentified_client.get(
            f"/api/v1/cables/poles/{self.pk}/"
        )
        self.assertEquals(resp.status_code, 401)

    def test_create_with_anonymous_user(self):
        resp = self.anonymous_client.post("/api/v1/cables/poles/")
        self.assertEquals(resp.status_code, 401)
        resp = self.unauthentified_client.post("/api/v1/cables/poles/")
        self.assertEquals(resp.status_code, 401)

    def test_update_with_anonymous_user(self):
        resp = self.anonymous_client.put(f"/api/v1/cables/poles/{self.pk}/")
        self.assertEquals(resp.status_code, 401)
        resp = self.unauthentified_client.put(
            f"/api/v1/cables/poles/{self.pk}/"
        )
        self.assertEquals(resp.status_code, 401)

    def test_partial_update_with_anonymous_user(self):
        resp = self.anonymous_client.patch(f"/api/v1/cables/poles/{self.pk}/")
        self.assertEquals(resp.status_code, 401)
        resp = self.unauthentified_client.patch(
            f"/api/v1/cables/poles/{self.pk}/"
        )
        self.assertEquals(resp.status_code, 401)

    def test_partial_delete_with_anonymous_user(self):
        resp = self.anonymous_client.delete(f"/api/v1/cables/poles/{self.pk}/")
        self.assertEquals(resp.status_code, 401)
        resp = self.unauthentified_client.delete(
            f"/api/v1/cables/poles/{self.pk}/"
        )
        self.assertEquals(resp.status_code, 401)


class PoleUnauthorizedAuthenticationTestCase(TestCase):
    """Class to test authentication/permission scheme for Pole and unauthorized user."""

    # fixture includes:
    # - at least 2 poles, 2 segments, 3 visits, 3 operations, 2 GeoAreas, 2 SensitiveAreas, 2 media
    # (pictures), 2 mortality cases
    # - It contains needed sinp_nomenclature items (stand for dictionanry for specific data)
    fixtures = ["test_nomenclatures.xml"]

    def setUp(self):
        self.user = createTestUser("user", "password")
        self.unauthorized_client = logTestUser("user", "password")
        # get pk from the first Pole
        self.pk = Pole.objects.all()[0].id

    # no restriction for read only by default with Django
    def test_get_list_with_unauthorized_user(self):
        resp = self.unauthorized_client.get("/api/v1/cables/poles/")
        self.assertEquals(resp.status_code, 200)

    # no restriction for read only by default with Django
    def test_get_detail_with_unauthorized_user(self):
        resp = self.unauthorized_client.get(f"/api/v1/cables/poles/{self.pk}/")
        self.assertEquals(resp.status_code, 200)

    def test_create_with_unauthorized_user(self):
        resp = self.unauthorized_client.post(
            f"/api/v1/cables/poles/{self.pk}/"
        )
        self.assertEquals(resp.status_code, 403)

    def test_update_with_unauthorized_user(self):
        resp = self.unauthorized_client.put(f"/api/v1/cables/poles/{self.pk}/")
        self.assertEquals(resp.status_code, 403)

    def test_partial_update_with_unauthorized_user(self):
        resp = self.unauthorized_client.patch(
            f"/api/v1/cables/poles/{self.pk}/"
        )
        self.assertEquals(resp.status_code, 403)

    def test_partial_delete_with_unauthorized_user(self):
        resp = self.unauthorized_client.delete(
            f"/api/v1/cables/poles/{self.pk}/"
        )
        self.assertEquals(resp.status_code, 403)


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
#     data["properties"]["owner"] = owne/manage.py test --pattern="tests_*.py"
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
