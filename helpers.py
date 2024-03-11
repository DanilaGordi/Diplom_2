import allure
from faker import Faker

@allure.step('Генерация тестовых данных российского пользователя')
def generate_user_data():
    fake = Faker('ru_RU')
    user_data = {
        "email": fake.email(),
        "password": fake.password(),
        "name": fake.first_name()
    }
    return user_data
