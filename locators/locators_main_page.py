from selenium.webdriver.common.by import By

class LocatorsMain:

    BUTTON_COOKIE = [By.ID, "rcc-confirm-button"]
    QUESTIONS = (By.ID, "accordion__heading-{}")
    ANSWER_QUESTIONS = (By.ID, "accordion__panel-{}")
    QUESTIONS_SCROLL = (By.ID, "accordion__heading-7")
