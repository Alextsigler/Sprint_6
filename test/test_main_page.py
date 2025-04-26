import allure
import pytest


class TestMain:

    @allure.title('Проверка всех вопросов и ответов с параметризацией')
    @pytest.mark.parametrize('num, expected_text', [
        (0, 'Сутки — 400 рублей'),
        (1, 'Пока что у нас так: один заказ'),
        (2, 'Допустим, вы оформляете заказ на 8 мая'),
        (3, 'Только начиная с завтрашнего дня'),
        (4, 'Пока что нет! Но если что-то срочное'),
        (5, 'Самокат приезжает к вам с полной зарядкой'),
        (6, 'Да, пока самокат не привезли'),
        (7, 'Да, обязательно. Всем самокатов')
    ])

    def test_click_questions_0(self, page_main_driver, num, expected_text):
        page_main_driver.click_to_cookie()
        page_main_driver.click_to_question(num)
        assert expected_text in page_main_driver.get_answer_question(num)
