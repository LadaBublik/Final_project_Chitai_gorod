from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common import StaleElementReferenceException
from time import sleep


class MainPage:
    """ Класс для работы с сайтом Читай-город """
    def __init__(self, driver):
        self._driver = driver
        self._driver.get("https://www.chitai-gorod.ru/")
        self._driver.maximize_window()
        self._driver.implicitly_wait(4)

    def auth(self, phone: str, code: str) -> str:
        self._driver.find_element(By.XPATH, '//span[text()="Войти"]').click()
        self._driver.find_element(By.CSS_SELECTOR, 'input.phone-input__input').send_keys(phone)
        self._driver.find_element(By.XPATH, '//span[text()="получить код"]').click()
        self._driver.find_element(By.CSS_SELECTOR, 'label.app-input__wrapper').send_keys(code) # отправляем неправильный код в поле введите код
        return self._driver.find_element(By.CSS_SELECTOR, 'span.sms-form__error').text

    def book_filtering(self) -> str:
        self._driver.find_element(By.CSS_SELECTOR,'.catalog__button').click() # Нажимаем на кнопку Каталог
        self._driver.find_element(By.XPATH,'(//span[@class="categories-menu__item-title"])[8]').click() # Выбираем категорию комиксы
        
        WebDriverWait(self._driver, 5).until(EC.text_to_be_present_in_element(
            (By.XPATH, '(//span[@class="catalog-template-filters__facet-title"])[2]'), 'Статус')) # ждем, когда появится выбор Статуса
        
        self._driver.find_element(By.XPATH,'(//span[@class="catalog-template-filters__list-item-label"])[4]').click() # отмечаем чек-бокс бестселлеры
        return self._driver.find_element(By.XPATH,'(//div[@class="product-title__head"])[1]').text
        
    def search_books(self, book_name: str):
        self._driver.find_element(By.CSS_SELECTOR, 'input.header-search__input').send_keys(book_name) 
        self._driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()

    def add_books(self):
        try:
            WebDriverWait(self._driver, 15).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'span.action-button__text')))
            buy_buttons = self._driver.find_elements(
                By.CSS_SELECTOR, 'span.action-button__text')
            counter = 0
            for btn in buy_buttons:
                btn.click()
                counter += 1
        except StaleElementReferenceException:
            print("Still can't click element with CCS_Selector:", 'span.action-button__text')
        return counter
    
    def get_cart(self):
        self._driver.get("https://www.chitai-gorod.ru/cart")

    def get_counter(self):
        txt = self._driver.find_element(
        By.CSS_SELECTOR,'div.wrapper').find_element(
            By.CSS_SELECTOR, 'span.app-title__append').text
        return int(txt)
    
    def get_empty_result_message(self):
        error_message = self._driver.find_element(By.CSS_SELECTOR, 'div.catalog-empty-result__description').find_element(By.CSS_SELECTOR, 'h4')
        return error_message.text

    def delete_book(self):
        self._driver.find_element(
        By.CSS_SELECTOR,'a[href="/product/python-s-nulya-3028159"]').find_element(
            By.CSS_SELECTOR, 'svg.cart-item__actions-icon').click()

    



