# Залогиниться
import requests

# def fest_autorizen(self):
payload = {
    "login": "testerw",
    "password": "qwerty"
}
r = requests.post('https://qa-scooter.praktikum-services.ru/api/v1/courier/login', data=payload)
print(r.text)