# from django.test import TestCase

# from cables.models import Pole
# from commons.tests.tests_commons import createTestUser, logTestUser


# class PoleTestCase(TestCase):

#     fixtures = ["nomenclatures.json"]
#     # From this fixtures, nomenclatures of type "owner" matched to pk 13 or 14 among nomenclature items

#     def setUp(self):
#         self.user2 = createTestUser(
#             "user2",
#             "password",
#             "view_pole",
#             "add_pole",
#             "change_pole",
#             "delete_pole",
#         )
#         self.authorized_client = logTestUser("user2", "password")

#     def test_all_pole_requests_OK(self):
#         # create 3 DB entries with owner pk = 13
#         for i in range(3):
#             resp = self.authorized_client.post("/api/cables/poles/", data={"owner": 13})
#             self.assertEquals(resp.status_code, 201)

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
