import allure
from conftest import *
from data import EndpointsUrl
from data import ErrorMessage


@allure.feature('Проверяем авторизацию пользователя')
class TestLoginUser:
    @allure.title('Тест авторизации существующего пользователя')
    def test_login_existing_user(self, user_data):
        payload = user_data
        response = requests.post(EndpointsUrl.LOGIN_USER, data=payload)
        assert response.status_code == 200 and response.json()['success']

    @allure.title('Тест авторизации с неверным логином')
    def test_login_user_incorrect_email_error(self, user_data):
        payload = user_data.copy()
        payload["email"] = 'new_incorrect_email@example.com'
        response = requests.post(EndpointsUrl.LOGIN_USER, data=payload)
        assert response.status_code == 401
        assert response.json()['message'] == ErrorMessage.INCORRECT_DATA

    @allure.title('Тест авторизации с неверным паролем')
    def test_login_user_incorrect_password_error(self, user_data):
        payload = user_data.copy()
        payload["password"] = 'new_incorrect_password'
        response = requests.post(EndpointsUrl.LOGIN_USER, data=payload)
        assert response.status_code == 401
        assert response.json()['message'] == ErrorMessage.INCORRECT_DATA
