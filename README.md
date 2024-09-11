<h1>Онлайн-магазин "Читай-город"</h1>

<h2>Описание</h2>

Проект по автоматизации тестирования основной функциональности сайта "Читай-город" на Python. 

Проект содержит 5 тестов на UI и 5 API-тестов. 

<h2>Окружение</h2>

<li>IDE: VSCode</li>
<li>WebDrivers: Chrome и Firefox</li>
<li>Версия Python: 3.12.4</li>
<li>Test Framework: pytest==8.3.2</li>

<h2>Структура проекта</h2>

1. Папка API_tests включает в себя:

<li>api_class.py 

Содержит методы для работы с сервером сайта "Читай-город,"</li>

<li>chitaigorod_api_test.py

Содержит 5 API-тестов приложения "Читай-город".</li>

2. Папка UI_tests включает в себя:

<li>ui_class.py 

Содержит методы для работы с сайтом "Читай-город,"</li>

<li>chitaigorod_ui_test.py

Содержит 5 тестов сайта "Читай-город".</li>

3. В файле constants.py содержатся постоянные данные, необходимые для запуска тестов:

URL сайта - https://www.chitai-gorod.ru/

Base_URL - https://web-gate.chitai-gorod.ru/api/

Api_key - Bearer Token, который необходимо получить перед запуском тестов на сайте магазина "Читай-город", предварительно авторизовавшись по номеру телефона

<h2>Зависимости и импорты</h2>

Для работы с данным проектом необходимо подключить следующие зависимости:
<li>selenium,</li>
<li>requests,</li>
<li>pytest,</li>
<li>allure.</li>

Для выполнения API-тестов необходимо выполнить:
```php
import requests
```

Для выполнения UI-тестов необходимо выполнить:
```php
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
```

Для создания отчета в Allure необходимо выполнить его импорт:
```php
import allure
```

<h2>Запуск автотестов</h2>

Для запуска автотестов необходимо ввести в терминале: 

`pytest chitaigorod_api_test.py` - API-тесты

`pytest chitaigorod_ui.py` - UI-тесты

Формирование отчета в Allure:

1. `python -m pytest --alluredir allure-results`
2. `allure serve allure-results`

