import pytest
import requests

from courier_api import *
from urls import TestAPIBaseLinks, TestAPICourierLinks


@pytest.fixture()
def test_user():
    response, login_pass = register_new_courier_and_return_login_password()
    yield response, login_pass

    sign_in = {
        "login": login_pass[0],
        "password": login_pass[1]
    }

    courier_signin = requests.post(TestAPIBaseLinks.main_url + TestAPICourierLinks.login_url, data=sign_in)
    courier_id = courier_signin.json()["id"]
    requests.delete(TestAPIBaseLinks.main_url + TestAPICourierLinks.login_url + str(courier_id))


@pytest.fixture
def courier_login(test_user):
    return test_user[1][0]


@pytest.fixture
def courier_password(test_user):
    return test_user[1][1]
