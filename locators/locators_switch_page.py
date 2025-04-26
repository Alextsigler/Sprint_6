from selenium.webdriver.common.by import By


class LocatorsSwitch:

    LOGO_YANDEX = (By.XPATH, "//img[@src='/assets/ya.svg']")
    FIELD_SEARCH_YANDEX = (By.XPATH, "/html/body/div[8]/div[2]/div[1]/div/div/div/div/div[1]/div[1]/div/div/button")

    LOGO_SAMOKAT = (By.XPATH, "//img[@src='/assets/scooter.svg']")
    TEXT_SAMOKAT = (By.XPATH, "//div[@class='Home_SubHeader__zwi_E' and text()='Привезём его прямо к вашей двери,']")

