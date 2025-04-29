import allure
import pytest


@allure.feature('Tests_Order')
class TestOrder:

    @pytest.mark.parametrize('name, last_name, adress, text, check, comment', [
        ('Александр', 'Андреевич', 'Москва', 'сутки', 'black', 'привези пж'),
        ('Андрей', 'Александрович', 'Питер', 'двое суток', 'grey', 'не срочно')
    ])
    @allure.title('Проверка Формы Заказа, через кнопку в headers')
    @allure.description('Описание провери формы заказа')
    def test_form_order_header(self, page_order_driver, name, last_name, adress, text, check, comment):
        page_order_driver.click_to_cookie()
        page_order_driver.click_to_order_header()
        page_order_driver.input_form_order(name, last_name, adress)
        page_order_driver.click_button_next()
        page_order_driver.input_form_rent(text, check, comment)
        page_order_driver.click_button_order_form()
        page_order_driver.click_button_yes()
        assert "Заказ оформлен" in page_order_driver.get_order_succsess()

    @pytest.mark.parametrize('name, last_name, adress, text, check, comment', [
        ('Александр', 'Андреевич', 'Москва', 'сутки', 'black', 'привези пж'),
        ('Андрей', 'Александрович', 'Питер', 'двое суток', 'grey', 'не срочно')
    ])
    @allure.title('Проверка Формы Заказа, через кнопку в body')
    @allure.description('Описание провери формы заказа')
    def test_form_driver_body(self, page_order_driver, name, last_name, adress, text, check, comment):
        page_order_driver.click_to_cookie()
        page_order_driver.scroll_to_order_body()
        page_order_driver.click_to_order_body()
        page_order_driver.input_form_order(name, last_name, adress)
        page_order_driver.click_button_next()
        page_order_driver.input_form_rent(text, check, comment)
        page_order_driver.click_button_order_form()
        page_order_driver.click_button_yes()
        assert "Заказ оформлен" in page_order_driver.get_order_succsess()