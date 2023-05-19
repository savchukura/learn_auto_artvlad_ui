import random

from generator.generator import generated_person
from locators.elements_page_locators import TextBoxPageLocators
from locators.elements_page_locators import CheckBoxPageLocators
from pages.base_page import BasePage


class TextBoxPage(BasePage):

    def fill_all_fields(self):
        person_info = next(generated_person())
        full_name = person_info.full_name
        email = person_info.email
        current_address = person_info.current_address
        permanent_address = person_info.permanent_address
        self.element_is_visible(TextBoxPageLocators.FULL_NAME).send_keys(full_name)
        self.element_is_visible(TextBoxPageLocators.EMAIL).send_keys(email)
        self.element_is_visible(TextBoxPageLocators.CURRENT_ADDRESS).send_keys(current_address)
        self.element_is_visible(TextBoxPageLocators.PERMANENT_ADDRESS).send_keys(permanent_address)
        self.element_is_visible(TextBoxPageLocators.SUBMIT).click()
        return full_name, email, current_address, permanent_address

    def check_filled_form(self):
        full_name = self.element_is_present(TextBoxPageLocators.CREATED_FULL_NAME).text.split(':')[1]
        email = self.element_is_present(TextBoxPageLocators.CREATED_EMAIL).text.split(':')[1]
        current_address = self.element_is_present(TextBoxPageLocators.CREATED_CURRENT_ADDRESS).text.split(':')[1]
        permanent_address = self.element_is_present(TextBoxPageLocators.CREATED_PERMANENT_ADDRESS).text.split(':')[1]
        return full_name, email, current_address, permanent_address


class CheckBoxPage(BasePage):

    def open_full_list(self):
        self.element_is_visible(CheckBoxPageLocators.EXPAND_ALL_BUTTON).click()

    def click_random_checkbox(self):
        item_list = self.elements_are_visible(CheckBoxPageLocators.ITEM_LIST)
        count = 21
        while count != 0:
            item = item_list[random.randint(1, 15)]
            if count > 0:
                self.go_to_element(item)
                item.click()
                count -= 1
            else:
                break

    def get_checked_checkboxes(self):
        checked_list = self.elements_are_present(CheckBoxPageLocators.CHECKED_ITEMS)
        data = []
        for box in checked_list:
            title_item = box.find_element("xpath", CheckBoxPageLocators.TITLE_ITEM)
            data.append(title_item.text)
        return str(data).replace(' ', '').replace('doc', '').replace('.', '').lower()

    def get_output_result(self):
        result_list = self.elements_are_present(CheckBoxPageLocators.OUTPUT_RESULT)
        data = []
        for item in result_list:
            data.append(item.text)
        return str(data).replace(' ', '').lower()
