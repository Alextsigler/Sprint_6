import allure

from locators.locators_main_page import LocatorsMain
from pages.base_page import BasePage


class PageMain(BasePage):

    @allure.step('Клик на куку')
    def click_to_cookie(self):
        self.click_element_with_wait(LocatorsMain.BUTTON_COOKIE)

    @allure.step('Клик на вопрос')
    def click_to_question(self, num):
        self.scroll_to_element(LocatorsMain.QUESTIONS_SCROLL)
        locator_q_formatted = self.format_locators(LocatorsMain.QUESTIONS, num)
        self.click_element_with_wait(locator_q_formatted)

    @allure.step('Получение ответа на вопрос')
    def get_answer_question(self, num):
        locator_q_formatted = self.format_locators(LocatorsMain.ANSWER_QUESTIONS, num)
        return self.get_text_element_with_wait(locator_q_formatted)
