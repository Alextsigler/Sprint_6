from selenium.webdriver.common.by import By


class LocatorsOrder:

    BUTTON_ORDER_HEADER = (By.XPATH, ".//button[@class='Button_Button__ra12g' and text()='Заказать']")
    BUTTON_ORDER_BODY = (By.XPATH, ".//button[@class='Button_Button__ra12g Button_Middle__1CSJM' and text()='Заказать']")

    """локаторы для формы заказа "Для кого самокат" """

    FIELD_NAME = (By.CSS_SELECTOR, "input[placeholder='* Имя']")
    FIELD_LAST_NAME = (By.CSS_SELECTOR, "input[placeholder='* Фамилия']")
    FIELD_ADRESS = (By.CSS_SELECTOR, "input[placeholder='* Адрес: куда привезти заказ']")
    FIELD_STANTION = (By.CSS_SELECTOR, "input[placeholder='* Станция метро']")
    SELECTED_STANTION = (By.XPATH, "//li[@class='select-search__row']//button[@value={}]")
    FIELD_PHONE = (By.CSS_SELECTOR, "input[placeholder='* Телефон: на него позвонит курьер']")

    BUTTON_NEXT = (By.XPATH, ".//button[@class='Button_Button__ra12g Button_Middle__1CSJM' and text()='Далее']")

    """Локаторы для формы заказа "Про аренду" """

    FIELD_DATA = (By.CSS_SELECTOR, "input[placeholder='* Когда привезти самокат']")
    SELECT_DATA = (By.XPATH, ".//div[contains(@class, 'react-datepicker__day react-datepicker__day--{}')]")
    FIELD_RENT = (By.XPATH, ".//div[@class='Dropdown-placeholder' and text()='* Срок аренды']")
    SELECTED_RENT = (By.XPATH, ".//div[@class='Dropdown-option' and text()='{}']")
    CHECK_BOX = (By.ID, "{}")
    FIELD_COMMENT = (By.CSS_SELECTOR, "input[placeholder='Комментарий для курьера']")
    BUTTON_ORDER_FORM = (By.XPATH, ".//button[@class='Button_Button__ra12g Button_Middle__1CSJM' and text()='Заказать']")
    BUTTON_YES = (By.XPATH, ".//button[@class='Button_Button__ra12g Button_Middle__1CSJM' and text()='Да']")

    TEXT_SUCSESS = (By.XPATH, ".//div[@class='Order_ModalHeader__3FDaJ']")
