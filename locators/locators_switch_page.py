from selenium.webdriver.common.by import By


class LocatorsSwitch:

    LOGO_YANDEX = (By.XPATH, "//img[@src='/assets/ya.svg']")
    FIELD_SEARCH_YANDEX = (By.XPATH, "//button[@class='dzen-desktop--geoblock__location-3m' and text()='Москва']")

    LOGO_SAMOKAT = (By.XPATH, "//img[@src='/assets/scooter.svg']")
    TEXT_SAMOKAT = (By.XPATH, "//div[@class='Home_SubHeader__zwi_E' and text()='Привезём его прямо к вашей двери,']")

