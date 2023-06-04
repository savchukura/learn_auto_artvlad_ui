import random
from selenium.webdriver.common.keys import Keys
from locators.practice_form_locators import PracticeFormPageLocators
from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from generator.generator import generated_person, generated_file, generate_subject
import os


class PracticeFormPage(BasePage):

    def fill_all_fields(self):
        personal = next(generated_person())
        file_name, path = generated_file()
        firstname = personal.firstname
        lastname = personal.lastname
        email = personal.email
        age = personal.age
        salary = personal.salary
        department = personal.department
        self.element_is_visible(WebTablePageLocators.ADD_BUTTON).click()
        self.element_is_visible(WebTablePageLocators.FIRSTNAME_INPUT).send_keys(firstname)
        self.element_is_visible(WebTablePageLocators.LASTNAME_INPUT).send_keys(lastname)
        self.element_is_visible(WebTablePageLocators.EMAIL_INPUT).send_keys(email)
        self.element_is_visible(WebTablePageLocators.AGE_INPUT).send_keys(age)
        self.element_is_visible(WebTablePageLocators.SALARY_INPUT).send_keys(salary)
        self.element_is_visible(WebTablePageLocators.DEPARTMENT_INPUT).send_keys(department)
        self.element_is_visible(WebTablePageLocators.SUBMIT_BUTTON).click()

        return [firstname, lastname, str(age), email, str(salary), department]

    def fill_form_fields(self):
        person = next(generated_person())
        file_name, path = generated_file()
        subject = generate_subject()
        self.element_is_visible(PracticeFormPageLocators.FIRST_NAME_INPUT).send_keys(person.firstname)
        self.element_is_visible(PracticeFormPageLocators.LAST_NAME_INPUT).send_keys(person.lastname)
        self.element_is_visible(PracticeFormPageLocators.EMAIL_NAME_INPUT).send_keys(person.email)

        gender_radio = self.element_is_present(PracticeFormPageLocators.GENDER_RADIO_BUTTONS)
        gender_radio.click()
        gender_name = gender_radio.find_element("xpath", PracticeFormPageLocators.GENDER_TEXT)

        date_of_birth = self.element_is_visible(PracticeFormPageLocators.DATA_OF_BIRTH_INPUT).get_attribute("value")

        self.element_is_visible(PracticeFormPageLocators.MOBILE_INPUT).send_keys(person.mobile)

        subject_name = subject[random.randint(0, 13)]
        self.element_is_visible(PracticeFormPageLocators.SUBJECT).send_keys(subject_name)
        self.element_is_visible(PracticeFormPageLocators.SUBJECT).send_keys(Keys.RETURN)

        hobbies_check_box = self.element_is_visible(PracticeFormPageLocators.HOBBIES_CHECK_BOXES)
        hobbies_check_box.click()
        hobbies_text = hobbies_check_box.find_element("xpath", PracticeFormPageLocators.HOBBIES_TEXT)

        self.element_is_present(PracticeFormPageLocators.UPLOAD_FILE_INPUT).send_keys(path)
        os.remove(path)

        self.element_is_visible(PracticeFormPageLocators.CURRENT_ADDRESS_INPUT).send_keys(person.current_address.split('\n'))

        self.go_to_element(self.element_is_present(PracticeFormPageLocators.STATE_DROP_DOWN))
        self.element_is_visible(PracticeFormPageLocators.STATE_DROP_DOWN).click()
        self.element_is_visible(PracticeFormPageLocators.STATE_INPUT).send_keys(Keys.RETURN)
        state_text = self.element_is_visible(PracticeFormPageLocators.STATE_DROP_DOWN)

        self.element_is_visible(PracticeFormPageLocators.CITY_DROP_DOWN).click()
        self.element_is_visible(PracticeFormPageLocators.CITY_INPUT).send_keys(Keys.RETURN)
        city_text = self.element_is_visible(PracticeFormPageLocators.CITY_DROP_DOWN)

        self.go_to_element(self.element_is_present(PracticeFormPageLocators.SUBMIT_BUTTON))
        self.element_is_visible(PracticeFormPageLocators.SUBMIT_BUTTON).click()

        return person, gender_name.text, hobbies_text.text, date_of_birth, file_name.split('\\')[-1], subject_name,\
            state_text.text, city_text.text

    def get_form_result(self):
        result_list = self.elements_are_present(PracticeFormPageLocators.RESULT_TABLE)
        data = []
        for item in result_list:
            data.append(item.text)
        return data

