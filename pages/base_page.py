from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def get_driver(self, url):
        """Метод открытия веб-приложения"""

        self.driver.get(url)

    def find_element_with_wait(self, locators):
        """Поиск элемента с ожиданием и возврат"""

        WebDriverWait(self.driver, timeout=10).until(
            expected_conditions.visibility_of_element_located(locators))
        return self.driver.find_element(*locators)

    def click_element_with_wait(self, locators):
        """Кликаем на элемент с ожиданием"""

        WebDriverWait(self.driver, timeout=10).until(
            expected_conditions.element_to_be_clickable(locators)).click()

    def get_text_element_with_wait(self, locators):
        """Получаем текст элемента с ожиданием"""

        return self.find_element_with_wait(locators).text

    def scroll_to_element(self, locators):
        """Скролим до полследнего вопроса"""

        element = self.driver.find_element(*locators)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def add_text_to_element(self, locators, text):
        """Добавляем текст в элемент"""

        self.find_element_with_wait(locators).send_keys(text)

    def format_locators(self, arg1, arg2):
        """Форматируем дублирующиеся локаторы (соединяем в один)

        arg1: локатор
        arg2: значение локатора

        """
        method, locator = arg1         # (By.ID, "accordion__heading-{}")
        locator = locator.format(arg2)  # "accordion__heading-{}" --> "accordion__heading-0"

        return (method, locator)   # (By.ID, "accordion__heading-0")

    def use_new_window(self):
        """Переход управления драйвера на новую вкладку"""

        WebDriverWait(self.driver, 10).until(lambda d: len(d.window_handles) == 2)
        self.driver.switch_to.window(self.driver.window_handles[-1])