from django.test import TestCase

from cables.models import Pole
from commons.tests.tests_commons import createTestUser, logTestUser


class PoleTestCase(TestCase):

    fixtures = ["nomenclatures.json"]
    # From this fixtures, nomenclatures of type "owner" matched to pk 13 or 14 among nomenclature items

    def setUp(self):
        #     self.user1 = createTestUser("user1", "password")
        #     self.anonymous_client = APIClient()
        #     self.unauthentified_client = logTestUser("user1", "wrong-password")
        #     self.unauthorized_client = logTestUser("user1", "password")
        self.user2 = createTestUser(
            "user2",
            "password",
            "view_pole",
            "add_pole",
            "change_pole",
            "delete_pole",
        )
        self.authorized_client = logTestUser("user2", "password")

    def test_post_with_authorized_user(self):
        # create 3 DB entries with owner pk = 13
        for i in range(3):
            resp = self.authorized_client.post(
                "/api/cables/poles/", data={"owner": 13}
            )
            self.assertEquals(resp.status_code, 201)

        # create 3 DB entries with owner pk = 14
        for i in range(3):
            resp = self.authorized_client.post(
                "/api/cables/poles/", data={"owner": 14}
            )
            self.assertEquals(resp.status_code, 201)

        pole_set = Pole.objects.all()
        self.assertEquals(len(pole_set), 6)
        resp = self.authorized_client.put(
            "/api/cables/poles/1/",
            data={
                "id": 1,
                "owner": 14,
                "geo_area": [],
                "sensitivity_area": [],
            },
        )
        self.assertEquals(resp.status_code, 200)
        pole = Pole.objects.get(pk=1)
        self.assertEquals(pole.owner_id, 14)

        resp = self.authorized_client.patch(
            "/api/cables/poles/1/", data={"owner": 13}
        )
        self.assertEquals(resp.status_code, 200)
        pole = Pole.objects.get(pk=1)
        self.assertEquals(pole.owner_id, 13)

        resp = self.authorized_client.get("/api/cables/poles/1/")
        self.assertEquals(resp.status_code, 200)
        self.assertEquals(resp.json()["id"], 1)

        resp = self.authorized_client.get("/api/cables/poles/")
        self.assertEquals(resp.status_code, 200)
        self.assertEquals(len(resp.json()), 6)
        self.assertIsInstance(resp.json()[0]["owner"], int)

        resp = self.authorized_client.get("/api/cables/poles-full/")
        self.assertEquals(resp.status_code, 200)
        self.assertEquals(len(resp.json()), 6)
        self.assertIsInstance(resp.json()[0]["owner"], dict)

    # # self.assertEquals(resp.json()[0]["owner"], 14)
    # resp = self.authorized_client.get("/api/cables/poles-full/", format="json")
    # self.assertEquals(resp.status_code, 200)

    # print(resp.json()[0]["owner"])
