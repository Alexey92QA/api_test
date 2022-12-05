import requests
import allure
from datetime import datetime

base_url = 'https://api.nasa.gov/planetary/apod'
auth = 'faJPYb2zCdNTA8C0ZV5An26T0sV5lif8z4DG8IEh'
to_date = datetime.utcnow().strftime("%Y-%m-%d")
fail_date = datetime(1900, 12, 4).strftime("%Y-%m-%d")


class TestClass():
    def test_positive(self):
        params_dict = {'api_key': auth, 'date': to_date}
        response = requests.get(base_url, params=params_dict)
        with allure.step(f"Запрос отправлен, смотрим код ответа - {response.status_code}"):
            assert response.status_code == 200, f"Неверный код ответа, получен {response.status_code}"

    def test_negative(self):
        params_dict = {'api_key': auth, 'date': fail_date}
        response = requests.get(base_url, params=params_dict)
        with allure.step(f"Запрос отправлен, смотрим код ответа {response.status_code}"):
            assert response.status_code == 400, f"Неверный код ответа, получен {response.status_code}"
        with allure.step(f"Запрос отправлен, посмотрим текст ошибки {response.json().get('msg')}"):
            f"Текст ошибки - {response.status_code}"
            assert response.json().get('msg') == 'Date must be between Jun 16, 1995 and ' + datetime.utcnow().strftime(
                "%b "
                "%d, "
                "%Y."), f"Неверный текст ошибки ответа, получено {response.json().get('msg')} "
