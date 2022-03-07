from django.test import TestCase
from rest_framework.test import APIClient

from cables.models import Point
from commons.tests.tests_commons import createTestUser, logTestUser


class PointAnonymousAuthenticationTestCase(TestCase):
    """Class to test authentication/permission scheme for Pole and anonymous user.

    Include tests for user trying to log-in with wrong password
    """

    # fixture includes:
    # - at least 2 points, 2 lines, 3 diagnosis, 3 operations, 2 GeoAreas, 2 SensitiveAreas, 2
    # media
    # (pictures), 2 mortality cases
    # - It contains needed sinp_nomenclature items (stand for dictionanry for specific data)
    fixtures = ["test_nomenclatures.xml", "test_cables.xml"]

    def setUp(self):
        self.anonymous_client = APIClient()
        # create user trying to log-in with wrong password
        self.user = createTestUser("user", "password")
        self.unauthentified_client = logTestUser("user", "wrong-password")
        # get pk from the first Segment
        self.pk = Point.objects.all()[0].id

    def test_get_list_with_anonymous_user(self):
        resp = self.anonymous_client.get("/api/v1/cables/points/")
        self.assertEquals(resp.status_code, 401)
        resp = self.unauthentified_client.get("/api/v1/cables/points/")
        self.assertEquals(resp.status_code, 401)

    def test_get_detail_with_anonymous_user(self):
        resp = self.anonymous_client.get(f"/api/v1/cables/points/{self.pk}/")
        self.assertEquals(resp.status_code, 401)
        resp = self.unauthentified_client.get(
            f"/api/v1/cables/points/{self.pk}/"
        )
        self.assertEquals(resp.status_code, 401)

    def test_create_with_anonymous_user(self):
        resp = self.anonymous_client.post("/api/v1/cables/points/")
        self.assertEquals(resp.status_code, 401)
        resp = self.unauthentified_client.post("/api/v1/cables/points/")
        self.assertEquals(resp.status_code, 401)

    def test_update_with_anonymous_user(self):
        resp = self.anonymous_client.put(f"/api/v1/cables/points/{self.pk}/")
        self.assertEquals(resp.status_code, 401)
        resp = self.unauthentified_client.put(
            f"/api/v1/cables/points/{self.pk}/"
        )
        self.assertEquals(resp.status_code, 401)

    def test_partial_update_with_anonymous_user(self):
        resp = self.anonymous_client.patch(f"/api/v1/cables/points/{self.pk}/")
        self.assertEquals(resp.status_code, 401)
        resp = self.unauthentified_client.patch(
            f"/api/v1/cables/points/{self.pk}/"
        )
        self.assertEquals(resp.status_code, 401)

    def test_partial_delete_with_anonymous_user(self):
        resp = self.anonymous_client.delete(
            f"/api/v1/cables/points/{self.pk}/"
        )
        self.assertEquals(resp.status_code, 401)
        resp = self.unauthentified_client.delete(
            f"/api/v1/cables/points/{self.pk}/"
        )
        self.assertEquals(resp.status_code, 401)


class PointUnauthorizedAuthenticationTestCase(TestCase):
    """Class to test authentication/permission scheme for Pole and unauthorized user."""

    # fixture includes:
    # - at least 2 points, 2 lines, 3 diagnosis, 3 operations, 2 GeoAreas, 2 SensitiveAreas, 2 media
    # (pictures), 2 mortality cases
    # - It contains needed sinp_nomenclature items (stand for dictionanry for specific data)
    fixtures = ["test_nomenclatures.xml", "test_cables.xml"]

    def setUp(self):
        self.user = createTestUser("user", "password")
        self.unauthorized_client = logTestUser("user", "password")
        # get pk from the first Pole
        self.pk = Point.objects.all()[0].id

    # no restriction for read only by default with Django
    def test_get_list_with_unauthorized_user(self):
        resp = self.unauthorized_client.get("/api/v1/cables/points/")
        self.assertEquals(resp.status_code, 200)

    # no restriction for read only by default with Django
    def test_get_detail_with_unauthorized_user(self):
        resp = self.unauthorized_client.get(
            f"/api/v1/cables/points/{self.pk}/"
        )
        self.assertEquals(resp.status_code, 200)

    def test_create_with_unauthorized_user(self):
        resp = self.unauthorized_client.post(
            f"/api/v1/cables/points/{self.pk}/"
        )
        self.assertEquals(resp.status_code, 403)

    def test_update_with_unauthorized_user(self):
        resp = self.unauthorized_client.put(
            f"/api/v1/cables/points/{self.pk}/"
        )
        self.assertEquals(resp.status_code, 403)

    def test_partial_update_with_unauthorized_user(self):
        resp = self.unauthorized_client.patch(
            f"/api/v1/cables/points/{self.pk}/"
        )
        self.assertEquals(resp.status_code, 403)

    def test_partial_delete_with_unauthorized_user(self):
        resp = self.unauthorized_client.delete(
            f"/api/v1/cables/points/{self.pk}/"
        )
        self.assertEquals(resp.status_code, 403)


class PointAuthorizedAuthenticationTestCase(TestCase):
    """Class to test authentication/permission scheme for Pole and unauthorized user."""

    # fixture includes:
    # - at least 2 points, 2 lines, 3 diagnosis, 3 operations, 2 GeoAreas, 2 SensitiveAreas, 2
    # media
    # (pictures), 2 mortality cases
    # - It contains needed sinp_nomenclature items (stand for dictionanry for specific data)
    fixtures = ["test_nomenclatures.xml", "test_cables.xml"]

    def setUp(self):
        self.anonymous_client = APIClient()
        # create authentified user
        self.user = createTestUser("user", "password")
        self.authentified_client = logTestUser("user", "password")

    def test_get_points(self):
        # owners = Item.objects.all().filter(type__mnemonic="owner")
        # first_owner_id = owners[0].id
        # print(first_owner_id)

        resp = self.authentified_client.get("/api/v1/cables/points/")
        self.assertEquals(resp.status_code, 200)

        # get id of first Pole
        pole_id = Point.objects.all()[0].id
        # get json data from this Pole
        resp = self.authentified_client.get(
            f"/api/v1/cables/points/{pole_id}/"
        )
        self.assertEquals(resp.status_code, 200)

    # # change owner value from these data to make put request thereafter
    # data["properties"]["owner"] = owne/manage.py test --pattern="tests_*.py"
    # )
    # self.assertEquals(resp.status_code, 200)
    # # change again the owner with patch request
    # resp = self.authorized_client.patch(
    #     f"/api/cables/points/edit/{first_id}/", data={"owner": owner_pk[0]}
    # )
    # self.assertEquals(resp.status_code, 200)
    # # test get method on a detail Pole (through edit ViewSet)
    # resp = self.authorized_client.get(
    #     f"/api/cables/points/edit/{first_id}/"
    # )
    # self.assertEquals(resp.status_code, 200)


#     # create owners (nomenclature items) needed to create points
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
#             "/api/cables/points/edit/",
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
#             "/api/cables/points/edit/",
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


#     # test get method on a list Pole (through edit ViewSet)
#     resp = self.authorized_client.get("/api/cables/points/edit/")
#     self.assertEquals(resp.status_code, 200)

#     # test get method on a detail Pole (through info ViewSet)
#     resp = self.authorized_client.get(
#         f"/api/cables/points/info/{first_id}/"
#     )
#     self.assertEquals(resp.status_code, 200)

#     # test get method on a list Pole (through info ViewSet)
#     resp = self.authorized_client.get("/api/cables/points/info/")
#     self.assertEquals(resp.status_code, 200)

#     # test delete method on a detail Pole
#     resp = self.authorized_client.delete(
#         f"/api/cables/points/edit/{first_id}/"
#     )
#     self.assertEquals(resp.status_code, 204)

#     # test get method returns 404
#     resp = self.authorized_client.get(
#         f"/api/cables/points/info/{first_id}/"
#     )
#     self.assertEquals(resp.status_code, 404)
