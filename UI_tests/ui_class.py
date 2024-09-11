from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from constants import *
import allure


class MainPage:
    """ Класс предоставляет методы для работы с сайтом Читай-город """
    def __init__(self, driver):
        self._driver = driver
        self._driver.get(ui_url)
        self._driver.maximize_window()
        self._driver.implicitly_wait(4)

    @allure.step("Авторизация с вводом неверного кода из смс")
    def auth(self, phone: str, code: str) -> str:
        self._driver.find_element(By.XPATH, '//span[text()="Войти"]').click()
        self._driver.find_element(
            By.CSS_SELECTOR, 'input.phone-input__input').send_keys(phone)
        self._driver.find_element(
            By.XPATH, '//span[text()="получить код"]').click()
        WebDriverWait(self._driver, 5).until(EC.visibility_of_element_located(
            (By.CSS_SELECTOR, '[placeholder="12345"]')))
        self._driver.find_element(
            By.CSS_SELECTOR, '[placeholder="12345"]').send_keys(code)
        return self._driver.find_element(
            By.CSS_SELECTOR, 'span.sms-form__error').text

    @allure.step("Фильтрация комиксов по бестселлерам")
    def book_filtering(self) -> str:
        self._driver.find_element(By.CSS_SELECTOR, '.catalog__button').click()
        self._driver.find_element(
            By.XPATH, '(//span[@class="categories-menu__item-title"])[8]'
            ).click()
        WebDriverWait(self._driver, 5).until(EC.text_to_be_present_in_element(
            (By.XPATH, '(//span[@class="catalog-template-filters__facet-title"])[2]'
             ), 'Статус'))
        self._driver.find_element(
            By.XPATH, '(//span[@class="catalog-template-filters__list-item-label"])[4]'
            ).click()
        return self._driver.find_element(
            By.XPATH, '(//div[@class="product-title__head"])[1]').text

    @allure.step("Поиск книги через поле поиска")
    def search_books(self, book_name: str):
        self._driver.find_element(
            By.CSS_SELECTOR, 'input.header-search__input').send_keys(book_name)
        self._driver.find_element(
            By.CSS_SELECTOR, 'button[type="submit"]').click()

    @allure.step("Изменение местоположения")
    def change_location(self) -> str:
        self._driver.find_element(
            By.XPATH, '//span[@class="header-city__title"]').click()
        self._driver.find_element(
            By.XPATH,
            '//div[@class="button change-city__button change-city__button--cancel light-blue"]'
            ).click()
        WebDriverWait(self._driver, 5).until(EC.element_to_be_clickable(
            (By.XPATH, '(//li[@class="city-modal__popular-item"])[2]')))
        self._driver.find_element(
            By.XPATH, '(//li[@class="city-modal__popular-item"])[2]').click()
        WebDriverWait(self._driver, 10).until(EC.text_to_be_present_in_element(
            (By.XPATH, '//span[@class="header-city__title"]'),
            "Россия, Санкт-Петербург"))
        return self._driver.find_element(
            By.XPATH, '//span[@class="header-city__title"]').text

    @allure.step("Добавление книги в корзину")
    def add_book(self):
        WebDriverWait(self._driver, 15).until(EC.element_to_be_clickable((
            By.XPATH, '//div[@class="popmechanic-close"]')))
        self._driver.find_element(
            By.XPATH, '//div[@class="popmechanic-main"]').find_element(
            By.XPATH, '//div[@class="popmechanic-close"]').click()
        WebDriverWait(self._driver, 15).until(
            EC.element_to_be_clickable((
                By.XPATH,
                '//button[@class="button cookie-notice__button white"]')))
        self._driver.find_element(
            By.XPATH, '//button[@class="button cookie-notice__button white"]'
            ).click()
        WebDriverWait(self._driver, 20, 5).until(EC.element_to_be_clickable((
            By.XPATH, '(//span[@class="action-button__text"])[3]')))
        self._driver.find_element(
            By.XPATH, '(//span[@class="action-button__text"])[3]').click()

    @allure.step("Открытие корзины")
    def get_cart(self):
        self._driver.get("https://www.chitai-gorod.ru/cart")

    @allure.step("Получение количества книг в корзине")
    def get_count_of_books_in_cart(self) -> str:
        return self._driver.find_element(
            By.CSS_SELECTOR, 'span.app-title__append').text

    @allure.step("Получение пустого результата поиска несуществующей книги")
    def get_empty_result_message(self) -> str:
        error_message = self._driver.find_element(
            By.CSS_SELECTOR, 'div.catalog-empty-result__description'
            ).find_element(By.CSS_SELECTOR, 'h4')
        return error_message.text
