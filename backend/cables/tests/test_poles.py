from django.test import TestCase
from django.utils.timezone import datetime
from sinp_nomenclatures.models import Item, Type

from commons.tests.tests_commons import createTestUser, logTestUser


class PoleTestCase(TestCase):

    # From this fixtures, nomenclatures of type "owner" matched to pk 13 or 14 among nomenclature items

    def setUp(self):
        self.user = createTestUser(
            "user",
            "password",
            "view_pole",
            "add_pole",
            "change_pole",
            "delete_pole",
        )
        self.authorized_client = logTestUser("user", "password")

        # create 2 owners (nomenclature items) needed to create poles
        type = Type.objects.create(
            code="code",
            mnemonic="owner",
            label="owner",
            status="VALID",
            created_by=self.user,
            create_date=datetime.today(),
            update_date=datetime.today(),
        )
        type.save()
        self.owner_pk = []
        for i in [1, 2]:
            item = Item.objects.create(
                type=type,
                code=f"owner{i}",
                mnemonic=f"owner{i}",
                label=f"owner{i}",
            )
            item.save()
            self.owner_pk.append(item.id)

    def test_create_pole_requests_OK(self):
        # create 3 DB entries with owner pk = self.owner_pk[0]
        resp = self.authorized_client.post(
            "/api/cables/poles/edit/",
            data={
                "type": "Feature",
                "geometry": {
                    "type": "Point",
                    "coordinates": [0, 0],
                },
                "properties": {
                    "owner": self.owner_pk[0],
                },
            },
            format="json",
        )
        self.assertEquals(resp.status_code, 201)
        resp = self.authorized_client.get("/api/cables/poles/edit/")
        self.assertEquals(resp.status_code, 200)
        self.assertEquals(len(resp.json()["features"]), 1)
        self.assertEquals(resp.json()["features"][0]["properties"]["owner"], 1)
        resp = self.authorized_client.get("/api/cables/poles/info/")
        self.assertEquals(resp.status_code, 200)
        self.assertEquals(len(resp.json()["features"]), 1)
        self.assertEquals(
            resp.json()["features"][0]["properties"]["owner"]["id"], 1
        )

    def test_fail_create_pole_requests_with_wrong_data(self):
        resp = self.authorized_client.post(
            "/api/cables/poles/edit/",
            data={"owner": "wrong"},
            format="json",
        )
        self.assertEquals(resp.status_code, 400)


#         # create 3 DB entries with owner pk = 14
#         for i in range(3):
#             resp = self.authorized_client.post("/api/cables/poles/", data={"owner": 14})
#             self.assertEquals(resp.status_code, 201)

#         pole_set = Pole.objects.all()
#         self.assertEquals(len(pole_set), 6)

#         first_id = Pole.objects.filter(owner=13)[0].id

#         resp = self.authorized_client.put(
#             f"/api/cables/poles/{first_id}/",
#             data={
#                 "id": first_id,
#                 "owner": 14,
#                 "geo_area": [],
#                 "sensitivity_area": [],
#             },
#         )
#         self.assertEquals(resp.status_code, 200)
#         pole = Pole.objects.get(pk=first_id)
#         self.assertEquals(pole.owner_id, 14)

#         resp = self.authorized_client.patch(f"/api/cables/poles/{first_id}/", data={"owner": 13})
#         self.assertEquals(resp.status_code, 200)
#         pole = Pole.objects.get(pk=first_id)
#         self.assertEquals(pole.owner_id, 13)

#         resp = self.authorized_client.get(f"/api/cables/poles/{first_id}/")
#         self.assertEquals(resp.status_code, 200)
#         self.assertEquals(resp.json()["id"], first_id)

#         resp = self.authorized_client.get("/api/cables/poles/")
#         self.assertEquals(resp.status_code, 200)
#         self.assertEquals(len(resp.json()), 6)
#         self.assertIsInstance(resp.json()[0]["owner"], int)

#         resp = self.authorized_client.get("/api/cables/poles-full/")
#         self.assertEquals(resp.status_code, 200)
#         self.assertEquals(len(resp.json()), 6)
#         self.assertIsInstance(resp.json()[0]["owner"], dict)

#         resp = self.authorized_client.get(f"/api/cables/poles/{first_id}/")
#         self.assertEquals(resp.status_code, 200)
#         self.assertIsInstance(resp.json()["owner"], int)

#         resp = self.authorized_client.get(f"/api/cables/poles-full/{first_id}/")
#         self.assertEquals(resp.status_code, 200)
#         self.assertIsInstance(resp.json()["owner"], dict)

#         poles = Pole.objects.all()
#         nb_before = len(poles)
#         resp = self.authorized_client.delete(f"/api/cables/poles/{first_id}/")
#         self.assertEquals(resp.status_code, 204)
#         poles = Pole.objects.all()
#         nb_after = len(poles)
#         self.assertEquals(nb_after, nb_before - 1)
#         resp = self.authorized_client.get(f"/api/cables/poles/{first_id}/")
#         self.assertEquals(resp.status_code, 404)
#         resp = self.authorized_client.get(f"/api/cables/poles-full/{first_id}/")
#         self.assertEquals(resp.status_code, 404)
