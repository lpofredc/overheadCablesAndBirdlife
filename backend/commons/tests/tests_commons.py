from django.contrib.auth.models import Permission
from rest_framework.test import APIClient

from users.models import User


def createTestUser(username, password, *perm_codename):
    """Method to create user with given username and password, with given permission set, to be used for test purpose.

    Args:
        username ([String]): user name
        password ([String]): password
        perm_codename ([*String]): list of strings matching to permission codename in django auth_permission table. Can contain 0, 1 or several permissions.

    Returns:
        [User]: a User to be used for tests, defined with given username, password and permissions
    """
    user = User.objects.create(username=username)
    user.set_password(password)
    for codename in perm_codename:
        perm = Permission.objects.get(codename=str(codename))
        user.user_permissions.add(perm)
    user.save()

    return user


def logTestUser(username, password):
    """Method to log user with given username and password.

    Args:
        username ([String]): user name
        password ([String]): password

    Returns:
        [APIClient]: a client to be used for tests, authentified with given username, password
    """
    client = APIClient()

    resp = client.post(
        "/api/v1/auth/jwt/create/",
        data={"username": username, "password": password},
        format="json",
    )

    # if token set to response (json response contains {"access": token}), token set to headers on every ongoing requests through client
    if "access" in resp.json():
        token = resp.json()["access"]
        client.credentials(HTTP_AUTHORIZATION=f"JWT {token}")

    return client
