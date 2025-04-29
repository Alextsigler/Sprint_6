# Sprint_6

установка allure = https://allurereport.org/docs/install-for-macos/
pip install -r requirements.txt - установка зависимостей
pytest test/ --alluredir=allure_results  - запуск тестов с отчетом allure
allure serve allure_results - открытие отчета в UI
pytest test/ - запуст тестов без отчета allure
allure generate allure_results - генерация отчета для открытия на другом устройстве

test_main_page.py - тесты вопросов на главной странице
test_order_page.py - тесты заказов через кнопки на главной странице в headers и body
test_switch_page.py - тесты переходов

base_page.py - описание базовых методов для всех страниц
page_main.py - описание шагов для проверки вопросов
page_order.py - описание шагов для проверки заказов
switch_page.py - описание шагов для проверки переходов