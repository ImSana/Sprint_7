import requests
import pytest

# Создание курьера
class TestCreatCurier:

    def test_creat_curier_sucsess(self):
        payload = {
        "login": 'testerw',
        "password": 'qwerty',
        "firstName": 'lozkaw'
    }
        r = requests.post('https://qa-scooter.praktikum-services.ru/api/v1/courier', data=payload)
        assert r.status_code == 201
        assert r.json()['data']['login'] == 'testerw'
        assert r.json()['data']['firstName'] == 'lozkaw'
