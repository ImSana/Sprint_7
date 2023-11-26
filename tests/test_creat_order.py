import requests

def test_updated_profile():
    updated_profile = {"name": "Николай Пржевальский", "about": "Первопроходец"}

    response = requests.patch("https://qa-mesto.praktikum-services.ru/api/users/me",
                              headers={'Authorization': 'введи_сюда_свой_токен'}, data=updated_profile)

    assert response.status_code == 200
    assert response.json()['data']['name'] == 'Николай Пржевальский'
    assert response.json()['data']['about'] == 'Первопроходец'