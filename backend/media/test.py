# from django.contrib.auth.models import Permission, User
# from django.test import Client, TestCase
# from rest_framework.authtoken.models import Token
# from rest_framework.test import APIClient

# from media.models import Media


# class MediaTestCase(TestCase):
#     def setUp(self):
#         Media.objects.create(media="lion")
#         self.user = User.objects.create(username="user")
#         self.user.set_password("password")
#         # permission = Permission.objects.get(name="Can add media")
#         # self.user.user_permissions.add(permission)
#         self.user.save()

#     def test_get(self):
#         m = Media.objects.all()
#         self.assertEqual(len(m), 1)
#         u = User.objects.get(username="user")
#         self.assertEquals(u.username, "user")
#         client = APIClient()
#         t = client.login(username="user", password="password")
#         self.assertTrue(t)

#         # # token = Token.objects.get(user__username="user")
#         resp = client.post(
#             "/auth/jwt/create/",
#             data={"username": "user", "password": "password"},
#             format="json",
#         )
#         token = resp.json()["access"]
#         client.credentials(HTTP_AUTHORIZATION=f"JWT {token}")

#         resp = client.get("/api/media/list/")
#         self.assertEquals(resp.status_code, 200)

#     def test_create(self):
#         u = User.objects.get(username="user")
#         permission = Permission.objects.get(name="Can add media")
#         u.user_permissions.add(permission)
#         client = APIClient()
#         t = client.login(username="user", password="password")
#         self.assertTrue(t)

#         # # token = Token.objects.get(user__username="user")
#         resp = client.post(
#             "/auth/jwt/create/",
#             data={"username": "user", "password": "password"},
#             format="json",
#         )
#         token = resp.json()["access"]
#         client.credentials(HTTP_AUTHORIZATION=f"JWT {token}")

#         resp = client.post(
#             "/api/media/list/", data={"media": "coucou"}, format="json"
#         )
#         self.assertEquals(resp.status_code, 201)
#         m = Media.objects.get(media="coucou")
#         self.assertEquals(m.media, "coucou")
#         resp = client.get("/api/media/list/")
#         self.assertEquals(len(resp.json()), 2)
