import random

from selenium.webdriver.common.by import By


class PracticeFormPageLocators:

    FIRST_NAME_INPUT = (By.CSS_SELECTOR, "input[id='firstName']")
    LAST_NAME_INPUT = (By.CSS_SELECTOR, "input[id='lastName']")
    EMAIL_NAME_INPUT = (By.CSS_SELECTOR, "input[id='userEmail']")

    # Radio buttons
    GENDER_RADIO_BUTTONS = (By.CSS_SELECTOR, f"div[class*='custom-control'] label[for='gender-radio-{random.randint(1, 3)}']")
    GENDER_TEXT = ".//ancestor::div[@class='custom-control custom-radio custom-control-inline']"

    MOBILE_INPUT = (By.CSS_SELECTOR, "input[id='userNumber']")
    DATA_OF_BIRTH_INPUT = (By.CSS_SELECTOR, "input[id='dateOfBirthInput']")

    SUBJECT = (By.CSS_SELECTOR, "input[id='subjectsInput']")

    HOBBIES_CHECK_BOXES = (By.CSS_SELECTOR, f"div[class*='custom-control'] label[for='hobbies-checkbox-{random.randint(1, 3)}']")
    HOBBIES_TEXT = ".//ancestor::div[@class='custom-control custom-checkbox custom-control-inline']"

    UPLOAD_FILE_INPUT = (By.CSS_SELECTOR, "input[id='uploadPicture']")

    CURRENT_ADDRESS_INPUT = (By.CSS_SELECTOR, "textarea[id='currentAddress']")

    STATE_DROP_DOWN = (By.CSS_SELECTOR, "div[id='state']")
    STATE_INPUT = (By.CSS_SELECTOR, "input[id='react-select-3-input']")
    STATE_TEXT = ".//ancestor::div[@class='custom-control custom-checkbox custom-control-inline']"

    CITY_DROP_DOWN = (By.CSS_SELECTOR, "div[id='city']")
    CITY_INPUT = (By.CSS_SELECTOR, "input[id='react-select-4-input']")

    SUBMIT_BUTTON = (By.CSS_SELECTOR, "button[id='submit']")

    # Table Result
    RESULT_TABLE = (By.XPATH, "//div[@class='table-responsive']//td[2]")
