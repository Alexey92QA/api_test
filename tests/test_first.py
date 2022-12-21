import requests
import allure
import credentials
import creating_date


class TestClass:
    def test_positive(self):
        params_dict = {'api_key': credentials.auth, 'date': creating_date.to_date}
        response = requests.get(credentials.base_url, params=params_dict)
        with allure.step(f"Запрос отправлен, смотрим код ответа - {response.status_code}"):
            assert response.status_code == 200, f"Неверный код ответа, получен {response.status_code}"

    def test_negative(self):
        params_dict = {'api_key': credentials.auth, 'date': creating_date.fail_date}
        response = requests.get(credentials.base_url, params=params_dict)
        with allure.step(f"Запрос отправлен, смотрим код ответа {response.status_code}"):
            assert response.status_code == 400, f"Неверный код ответа, получен {response.status_code}"
        with allure.step(f"Запрос отправлен, посмотрим текст ошибки {response.json().get('msg')}"):
            f"Текст ошибки - {response.status_code}"
            assert response.json().get('msg') == 'Date must be between Jun 16, 1995 and ' + creating_date.datetime.utcnow().strftime(
                "%b "
                "%d, "
                "%Y."), f"Неверный текст ошибки ответа, получено {response.json().get('msg')} "
