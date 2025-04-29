import allure

import urls


@allure.feature('Tests_Switch')
class TestSwitch:

    @allure.title('Проверка перехода по лого Яндекс')
    def test_switch_logo_yandex(self, page_switch_driver):
        page_switch_driver.click_to_element_yandex()
        page_switch_driver.new_windows()
        page_switch_driver.wait_element_yandex()
        assert page_switch_driver.get_current_url() == urls.URL_DZEN

    @allure.title('Проверка перехода по лого Самокат')
    def test_switch_logo_samokat(self, page_switch_driver):
        page_switch_driver.click_to_element_samokat()
        page_switch_driver.wait_element_samokat()
        assert page_switch_driver.get_current_url() == urls.URL_GLOBAL
