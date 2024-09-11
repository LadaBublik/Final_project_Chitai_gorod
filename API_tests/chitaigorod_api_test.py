from API_tests.api_class import ChitaigorodApi
from constants import *
import allure

api = ChitaigorodApi(api_url)

@allure.title("Поиск книги по ее названию")
@allure.description("Найти книгу 'Python'")
@allure.feature("GET")
@allure.severity(allure.severity_level.BLOCKER)
def test_search_book():
    body = api.search_book_by_name('Python')
    with allure.step("Проверить, что длина списка в результате приходит больше нуля"):
        assert len(body) > 0


@allure.title("Поиск книг по фильтру новинки")
@allure.description("Найти новинки и проверить id первой")
@allure.feature("GET")
@allure.severity(allure.severity_level.CRITICAL)
def test_filter():
    body = api.book_filtering('1')
    with allure.step("Проверить id первой книги из списка"):
        assert body == '3062342'


@allure.title("Поиск книг по категории")
@allure.description("Найти книги по категории 'Календари 2025'")
@allure.feature("GET")
@allure.severity(allure.severity_level.CRITICAL)
def test_by_category():
    body = api.search_book_by_category({'slug': '110684'})
    with allure.step("Проверить, что название категории 'Календари 2025'"):
        assert body == "Календари 2025"


@allure.title("Добавление книги в корзину")
@allure.description("Найти, добавить книгу 'Python' в корзину и проверить статус-код")
@allure.feature("POST")
@allure.severity(allure.severity_level.BLOCKER)
def test_add_book():
    api.search_book_by_name('Python')
    body = api.add_book()
    with allure.step("Проверить, что статус код = 200 после добавления книги"):
        assert body == 200


@allure.title("Удаление книги из корзины")
@allure.description("Найти, добавить книгу 'Python' в корзину и удалить ее")
@allure.feature("DELETE")
@allure.severity(allure.severity_level.CRITICAL)
def test_delete_book_from_cart():
    api.search_book_by_name('Python')
    api.add_book()
    book_id = api.get_cart()
    deleted_book = api.delete_book(book_id)
    with allure.step("Проверить, что статус код = 204 после удаления книги"):
        assert deleted_book == 204
