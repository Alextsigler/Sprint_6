import allure

from locators.locators_main_page import LocatorsMain
from locators.locators_order_page import LocatorsOrder
from pages.base_page import BasePage
import helpers
import time


class PageOrder(BasePage):

    @allure.step('Клик на куку')
    def click_to_cookie(self):
        self.click_element_with_wait(LocatorsMain.BUTTON_COOKIE)

    @allure.step('Клик на кнопку "Заказать" в headers')
    def click_to_order_header(self):
        self.click_element_with_wait(LocatorsOrder.BUTTON_ORDER_HEADER)

    @allure.step('Клик на кнопку "Заказать" в body')
    def click_to_order_body(self):
        self.click_element_with_wait(LocatorsOrder.BUTTON_ORDER_BODY)

    @allure.step('Заполняем форму "Для кого самокат"')
    def input_form_order(self, name, last_name, adress):
        """Заполняем поле name"""
        self.add_text_to_element(LocatorsOrder.FIELD_NAME, name)

        """Заполняем поле last_name"""
        self.add_text_to_element(LocatorsOrder.FIELD_LAST_NAME, last_name)

        """Заполняем поле adress"""
        self.add_text_to_element(LocatorsOrder.FIELD_ADRESS, adress)

        """Нажимаем на поле станции для открытия выпадашки"""
        self.click_element_with_wait(LocatorsOrder.FIELD_STANTION)

        """Форматируем локатор для выбора разных станций и нажимаем на него"""
        format_locator = self.format_locators(LocatorsOrder.SELECTED_STANTION, helpers.random_num())
        self.click_element_with_wait(format_locator)

        """Заполняем поле phone"""
        self.add_text_to_element(LocatorsOrder.FIELD_PHONE, helpers.random_phone())

    @allure.step('Клик на кнопку "Далее"')
    def click_button_next(self):
        self.click_element_with_wait(LocatorsOrder.BUTTON_NEXT)

    @allure.step('Заполняем форму "Про аренду"')
    def input_form_rent(self, text, check_box, comment):
        self.click_element_with_wait(LocatorsOrder.FIELD_DATA)

        """Формируем локатор для генерации рандомного выбора даты"""
        locator_format = self.format_locators(LocatorsOrder.SELECT_DATA, helpers.random_data())
        self.click_element_with_wait(locator_format)

        self.click_element_with_wait(LocatorsOrder.FIELD_RENT)

        """Формируем локатор для генерации рандомного выбора времени аренды"""
        locator_format_rent = self.format_locators(LocatorsOrder.SELECTED_RENT, text)
        self.click_element_with_wait(locator_format_rent)

        """Формируем локатор для генерации выбора рандомного чек-бокса"""
        locator_check_box = self.format_locators(LocatorsOrder.CHECK_BOX, check_box)
        self.click_element_with_wait(locator_check_box)

        self.add_text_to_element(LocatorsOrder.FIELD_COMMENT, comment)

    @allure.step('Клик на кнопку "Заказать" в форме заказа')
    def click_button_order_form(self):
        self.click_element_with_wait(LocatorsOrder.BUTTON_ORDER_FORM)

    @allure.step('Клик на кнопку "Да"')
    def click_button_yes(self):
        self.click_element_with_wait(LocatorsOrder.BUTTON_YES)

    @allure.step('Получаем текс "Заказ оформлен"')
    def get_order_succsess(self):
        return self.get_text_element_with_wait(LocatorsOrder.TEXT_SUCSESS)

    @allure.step('Скролим до кнопку "Заказать" в body')
    def scroll_to_order_body(self):
        self.scroll_to_element(LocatorsOrder.BUTTON_ORDER_BODY)
