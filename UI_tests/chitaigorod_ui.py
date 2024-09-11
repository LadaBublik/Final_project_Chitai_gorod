from selenium import webdriver
from UI_tests.ui_class import MainPage
from UI_tests.data import *
import allure


@allure.title("Авторизация с неверным кодом")
@allure.description("Авторизация на сайте с неправильным паролем для проверки ошибки")
@allure.feature("AUTH")
@allure.severity(allure.severity_level.NORMAL)
def test_authrization():
    driver = webdriver.Firefox()
    main_page = MainPage(driver)
    result = main_page.auth(phone, code)
    with allure.step("Проверить текст ошибки"):
        assert result == 'Пожалуйста, проверьте код из СМС'
    driver.quit()


@allure.title("Изменение местоположения")
@allure.description("Изменение местоположения пользователя и проверка его отображения на сайте")
@allure.feature("CHAHGE")
@allure.severity(allure.severity_level.CRITICAL)
def test_change_location():
    driver = webdriver.Chrome()
    main_page = MainPage(driver)
    result = main_page.change_location()
    with allure.step("Проверить, что отображается выбранный город"):
        assert result == 'Россия, Санкт-Петербург'
    driver.quit()


@allure.title("Фильтрация комиксов по бестселлерам")
@allure.description("Отфильтровать комиксы по бестселлерам, для проверки работоспособности чек-боксов")
@allure.feature("GET")
@allure.severity(allure.severity_level.CRITICAL)
def test_filtering():
    driver = webdriver.Firefox()
    main_page = MainPage(driver)
    name_book = main_page.book_filtering()
    with allure.step("Проверить, что отображается первый комикс из фильтра"):
        assert name_book == "Блэксэд. Книга 5: Итак, все падает. Часть вторая"
    driver.quit()


@allure.title("Поиск книги по названию и добавление её в корзину")
@allure.description("Найти книгу по названию, нажать 'Купить' и проверить, что в корзине появился 1 товар")
@allure.feature("ADD")
@allure.severity(allure.severity_level.BLOCKER)
def test_add_book():
    driver = webdriver.Firefox()
    main_page = MainPage(driver)
    main_page.search_books(book_name)
    main_page.add_book()
    main_page.get_cart()
    as_is = main_page.get_count_of_books_in_cart()
    with allure.step("Проверить, что в корзине содержится 1 товар"):
        assert as_is == "1 товар"
    driver.quit()


@allure.title("Поиск несуществующей книги")
@allure.description("Проверка сообщения при поиске несуществующей книги")
@allure.feature("GET")
@allure.severity(allure.severity_level.CRITICAL)
def test_empty_search_result():
    driver = webdriver.Chrome()
    main_page = MainPage(driver)
    main_page.search_books('dfghsdgfkjhbs')
    msg = main_page.get_empty_result_message()
    with allure.step("Проверить, какой отображается текст, при поиске несуществующей книги"):
        assert msg == 'Похоже, у нас такого нет'
    driver.quit()
