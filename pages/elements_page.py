import base64
import os
import random
import time

import requests
from selenium.common import TimeoutException

from generator.generator import generated_person, generated_file
from locators.elements_page_locators import TextBoxPageLocators, DynamicPropertiesPageLocators
from locators.elements_page_locators import CheckBoxPageLocators
from locators.elements_page_locators import RadioButtonPageLocators, UploadAndDownloadPageLocators
from locators.elements_page_locators import WebTablePageLocators, ButtonsPageLocators, LinksPageLocators
from pages.base_page import BasePage
from selenium.webdriver.common.by import By


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


class RadioButtonPage(BasePage):

    def click_on_radio_button(self, choice):
        choices = {'yes': RadioButtonPageLocators.YES_RADIOBUTTON,
                   'impressive': RadioButtonPageLocators.IMPRESSIVE_RADIOBUTTON,
                   'no': RadioButtonPageLocators.NO_RADIOBUTTON}

        self.element_is_visible(choices[choice]).click()

    def get_output_result(self):
        return self.element_is_present(RadioButtonPageLocators.OUTPUT_RESULT).text


class WebTablePage(BasePage):

    def add_new_person(self):
        count = 1
        while count != 0:
            personal_info = next(generated_person())
            firstname = personal_info.firstname
            lastname = personal_info.lastname
            email = personal_info.email
            age = personal_info.age
            salary = personal_info.salary
            department = personal_info.department
            self.element_is_visible(WebTablePageLocators.ADD_BUTTON).click()
            self.element_is_visible(WebTablePageLocators.FIRSTNAME_INPUT).send_keys(firstname)
            self.element_is_visible(WebTablePageLocators.LASTNAME_INPUT).send_keys(lastname)
            self.element_is_visible(WebTablePageLocators.EMAIL_INPUT).send_keys(email)
            self.element_is_visible(WebTablePageLocators.AGE_INPUT).send_keys(age)
            self.element_is_visible(WebTablePageLocators.SALARY_INPUT).send_keys(salary)
            self.element_is_visible(WebTablePageLocators.DEPARTMENT_INPUT).send_keys(department)
            self.element_is_visible(WebTablePageLocators.SUBMIT_BUTTON).click()
            count -=1
            return [firstname, lastname, str(age), email, str(salary), department]

    def check_new_added_person(self):
        people_list = self.elements_are_present(WebTablePageLocators.FULL_PEOPLE_LIST)
        data = []
        for item in people_list:
            data.append(item.text.splitlines())
        return data

    def search_some_person(self, key_word):
        self.element_is_visible(WebTablePageLocators.SEARCH_INPUT).send_keys(key_word)

    def check_search_person(self):
        delete_button = self.element_is_present(WebTablePageLocators.DELETE_BUTTON)
        row = delete_button.find_element("xpath", WebTablePageLocators.ROW_PARENT)
        return row.text.splitlines()

    def update_person_info(self):
        person_info = next(generated_person())
        age = person_info.age
        self.element_is_visible(WebTablePageLocators.UPDATE_BUTTON).click()
        self.element_is_visible(WebTablePageLocators.AGE_INPUT).clear()
        self.element_is_visible(WebTablePageLocators.AGE_INPUT).send_keys(age)
        self.element_is_visible(WebTablePageLocators.SUBMIT_BUTTON).click()
        return str(age)

    def delete_person(self):
        self.element_is_visible(WebTablePageLocators.DELETE_BUTTON).click()

    def check_deleted(self):
        return self.element_is_present(WebTablePageLocators.NO_ROWS).text

    def select_up_to_some_rows(self):
        count = [5, 10, 20, 25, 50, 100]
        data = []
        for x in count:
            count_row_button = self.element_is_visible(WebTablePageLocators.COUNT_ROW_LIST)
            self.go_to_element(count_row_button)
            count_row_button.click()
            self.element_is_visible((By.CSS_SELECTOR, f"option[value='{x}")).click()
            data.append(self.check_count_rows())
        return data

    def check_count_rows(self):
        list_rows = self.elements_are_present(WebTablePageLocators.FULL_PEOPLE_LIST)
        return len(list_rows)


class ButtonsPage(BasePage):

    def click_on_different_button(self, type_click):
        if type_click == "double":
            self.action_double_click(self.element_is_visible(ButtonsPageLocators.DOUBLE_BUTTON))
            return self.check_clicked_on_the_button(ButtonsPageLocators.SUCCESS_DOUBLE)
        if type_click == "right":
            self.action_right_click(self.element_is_visible(ButtonsPageLocators.RIGHT_CLICK_BUTTON))
            return self.check_clicked_on_the_button(ButtonsPageLocators.SUCCESS_RIGHT)
        if type_click == "click":
            self.element_is_visible(ButtonsPageLocators.CLICK_ME_BUTTON).click()
            return self.check_clicked_on_the_button(ButtonsPageLocators.SUCCESS_CLICK_ME)

    def check_clicked_on_the_button(self, element):
        return self.element_is_present(element).text


class LinksPage(BasePage):

    def check_new_tab_simple_link(self):
        simple_link = self.element_is_visible(LinksPageLocators.SIMPLE_LINK)
        link_href = simple_link.get_attribute('href')
        request = requests.get(link_href)
        if request.status_code == 200:
            simple_link.click()
            self.driver.switch_to.window(self.driver.window_handles[1])
            url = self.driver.current_url
            return link_href, url
        else:
            return link_href, request.status_code

    def check_broken_link(self, url):
        request = requests.get(url)
        if request.status_code == 200:
            self.element_is_present(LinksPageLocators.BAD_REQUEST).click()
        else:
            return request.status_code


class UploadAndDownloadPage(BasePage):

    def upload_file(self):
        file_name, path = generated_file()
        self.element_is_present(UploadAndDownloadPageLocators.UPLOAD_FILE).send_keys(path)
        os.remove(path)
        text = self.element_is_present(UploadAndDownloadPageLocators.UPLOADED_RESULT).text
        return file_name.split('\\')[-1], text.split('\\')[-1]

    def download_file(self):
        link = self.element_is_present(UploadAndDownloadPageLocators.DOWNLOAD_BUTTON).get_attribute('href')
        link_b = base64.b64decode(link)
        path_name_file = os.path.abspath(f"../files/test{random.randint(0, 999)}.jpeg")
        with open(path_name_file, 'wb+') as f:
            offset = link_b.find(b'\xff\xd8')
            f.write(link_b[offset:])
            check_file = os.path.exists(path_name_file)
            f.close()
        os.remove(path_name_file)
        return check_file


class DynamicPropertiesPage(BasePage):

    def check_enable_button(self):
        try:
            self.element_is_clickable(DynamicPropertiesPageLocators.ENABLE_BUTTON)
        except TimeoutException:
            return False
        return True

    def check_changed_of_color(self):
        color_button = self.element_is_present(DynamicPropertiesPageLocators.COLOR_CHANGE_BUTTON)
        color_button_before = color_button.value_of_css_property('color')
        time.sleep(5)
        color_button_after = color_button.value_of_css_property('color')
        return color_button_before, color_button_after

    def check_appear_button(self):
        try:
            self.element_is_visible(DynamicPropertiesPageLocators.VISIBLE_AFTER_FIVE_SEC_BUTTON)
        except TimeoutException:
            return False
        return True
