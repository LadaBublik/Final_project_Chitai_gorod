import requests
from constants import *
import allure


class ChitaigorodApi:
    """Метод для работы с сервером сайта "Читай-город"""
    def __init__(self, url):
        self.url = url

    @allure.step("API. Поиск книги по названию")
    def search_book_by_name(self, params_to_add: str) -> dict:
        my_headers = api_key
        resp = requests.get(
            self.url + 'v1/recommend/semantic', headers=my_headers,
            params=params_to_add)
        return resp.json()['data']

    @allure.step("API. Поиск книги по фильтру")
    def book_filtering(self, params_to_add: str) -> str:
        my_headers = api_key
        resp = requests.get(
            self.url + 'v2/products', headers=my_headers,
            params=params_to_add)
        return resp.json()['data'][0]['id']

    @allure.step("API. Поиск книги по категории")
    def search_book_by_category(self, params_to_add: dict) -> str:
        my_headers = api_key
        resp = requests.get(
            self.url + 'v1/categories/tree', headers=my_headers,
            params=params_to_add)
        return resp.json()['data']['info']['title']

    @allure.step("API. Добавление книги в корзину")
    def add_book(self) -> int:
        my_headers = api_key
        book = {
            "id": 2978800,
            "adData": {"item_list_name": "search", "product_shelf": ""}
            }
        resp = requests.post(
            self.url + 'v1/cart/product', headers=my_headers, json=book)
        return resp.status_code

    @allure.step("API. Переход на страницу корзины")
    def get_cart(self) -> int:
        my_headers = api_key
        resp = requests.get(
            self.url + 'v1/cart', headers=my_headers)
        return resp.json()['products'][0]['id']

    @allure.step("API. Удаление книги из корзины")
    def delete_book(self, id: str) -> int:
        my_headers = api_key
        resp = requests.delete(
            self.url + 'v1/cart/product/' + str(id), headers=my_headers)
        return resp.status_code
