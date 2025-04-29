import allure

from locators.locators_switch_page import LocatorsSwitch
from pages.base_page import BasePage


class SwitchPage(BasePage):

    @allure.step('Клик на лого "Яндекс" в headers')
    def click_to_element_yandex(self):
        self.click_element_with_wait(LocatorsSwitch.LOGO_YANDEX)

    @allure.step('Переводим управление драйвером на новую вкладку')
    def new_windows(self):
        self.use_new_window()

    @allure.step('Ожидаем появления элемента на странице яндекса')
    def wait_element_yandex(self):
        self.find_element_with_wait(LocatorsSwitch.FIELD_SEARCH_YANDEX)

    @allure.step('Клик на лого Самокат в headers')
    def click_to_element_samokat(self):
        self.click_element_with_wait(LocatorsSwitch.LOGO_SAMOKAT)

    @allure.step('Ожидаем появления элемента на странице Самокат')
    def wait_element_samokat(self):
        self.find_element_with_wait(LocatorsSwitch.TEXT_SAMOKAT)

    @allure.step('Получаем нынешний URL страницы')
    def get_current_url(self):
        URL = self.driver.current_url
        return URL

