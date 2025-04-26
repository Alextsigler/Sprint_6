import allure
import pytest

from selenium import webdriver
from selenium.webdriver.firefox.options import Options

import urls
from pages.page_main import PageMain
from pages.page_order import PageOrder
from pages.switch_page import SwitchPage


@pytest.fixture
def firefox_driver():

    """Фикстура для создания драйвера браузера"""

    options = Options()
    options.add_argument('--window-size=1920,1080')
    firefox_driver = webdriver.Firefox(options=options)
    yield firefox_driver
    firefox_driver.quit()


@pytest.fixture
def page_main_driver(firefox_driver):
    """Фикстура для инициализации драйвера для страницы page_main"""

    page_main_driver = PageMain(firefox_driver)
    page_main_driver.get_driver(urls.url_global)
    yield page_main_driver


@pytest.fixture
def page_order_driver(firefox_driver):
    """Фикстура для инициализации драйвера для страницы page_order"""

    page_order_driver = PageOrder(firefox_driver)
    page_order_driver.get_driver(urls.url_global)
    yield page_order_driver

@pytest.fixture
def page_switch_driver(firefox_driver):
    """Фикстура для инициализации драйвера для страницы page_switch"""

    page_switch_driver = SwitchPage(firefox_driver)
    page_switch_driver.get_driver(urls.url_order)
    yield page_switch_driver
