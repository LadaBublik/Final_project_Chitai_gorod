from selenium import webdriver
from main_page import MainPage
from data import *
from time import sleep
    
# 1. ввод неверного кода и сравнение ошибок
def test_authrization():
    driver = webdriver.Chrome()
    main_page = MainPage(driver)

    result = main_page.auth(phone, code)
    assert result == 'Пожалуйста, проверьте код из СМС'
    driver.quit()

# 2. фильтрация книг
def test_filtering():
    driver = webdriver.Chrome()
    main_page = MainPage(driver)
    
    name_book = main_page.book_filtering()
    assert name_book == "Блэксэд. Книга 5: Итак, все падает. Часть вторая"
    driver.quit()

# 3. Поиск книги по названию и добавление найденных книг в корзину
def test_add_book():
    driver = webdriver.Chrome()
    main_page = MainPage(driver)
    
    main_page.search_books(book_name)  
     
    to_be = main_page.add_books()  

    main_page.get()
    as_is = main_page.get_counter()   
    
    assert as_is == to_be
    driver.quit()

def test_empty_search_result():
    driver = webdriver.Chrome()
    main_page = MainPage(driver)
    main_page.search_books('dfghsdgfkjhbs')
    msg = main_page.get_empty_result_message()
    assert msg == 'Похоже, у нас такого нет'
    driver.quit()

# 5. удаление книги из корзины
def test_delete_book():
    driver = webdriver.Chrome()
    main_page = MainPage(driver)
    main_page.search_books(book_name)  
    main_page.add_books()  
    main_page.get_cart()
    main_page.delete_book()
    driver.quit()























