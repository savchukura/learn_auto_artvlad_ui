import allure

from pages.elements_page import TextBoxPage, WebTablePage, ButtonsPage, LinksPage, UploadAndDownloadPage, \
    DynamicPropertiesPage
from pages.elements_page import CheckBoxPage
from pages.elements_page import RadioButtonPage
import time
import random


@allure.suite("Elements")
class TestElements:

    @allure.feature("TextBox")
    class TestTextBox:

        @allure.title('Check TextBox')
        def test_text_box(self, driver):
            text_box_page = TextBoxPage(driver, "https://demoqa.com/text-box")
            text_box_page.open()
            full_name, email, current_address, permanent_address = text_box_page.fill_all_fields()
            output_name, output_email, output_current_address, output_permanent_address = text_box_page.check_filled_form()
            assert full_name == output_name, "full name incorrect"
            assert email == output_email, "email incorrect"
            assert current_address == output_current_address, "current_address incorrect"
            assert permanent_address == output_permanent_address, "permanent address incorrect"
            time.sleep(3)

    @allure.feature("CheckBox")
    class TestCheckBox:

        @allure.title('Check CheckBox')
        def test_check_box(self, driver):
            check_box_page = CheckBoxPage(driver, 'https://demoqa.com/checkbox')
            check_box_page.open()
            check_box_page.open_full_list()
            check_box_page.click_random_checkbox()
            input_checkbox = check_box_page.get_checked_checkboxes()
            output_result = check_box_page.get_output_result()
            print(input_checkbox)
            print(output_result)
            assert input_checkbox == output_result, "checkboxes have not been selected"
            time.sleep(1)

        def cycle(self, driver):
            for i in range(10):
                self.test_check_box(driver)

    @allure.feature("RadioButton")
    class TestRadioButton:

        @allure.title('Check RadioButton')
        def test_radio_button(self, driver):
            radio_button_page = RadioButtonPage(driver, 'https://demoqa.com/radio-button')
            radio_button_page.open()
            radio_button_page.click_on_radio_button("yes")
            output_yes = radio_button_page.get_output_result()
            radio_button_page.click_on_radio_button("impressive")
            output_impressive = radio_button_page.get_output_result()
            radio_button_page.click_on_radio_button("no")
            output_no = radio_button_page.get_output_result()
            assert output_yes == "Yes", "Yes have not been selected"
            assert output_impressive == "Impressive", "Impressive have not been selected"
            assert output_no == "No", "No have not been selected"

    @allure.feature("WebTable")
    class TestWebTable:

        @allure.title('Check CheckBox')
        def test_web_tabla_add_person(self, driver):
            web_table_page = WebTablePage(driver, 'https://demoqa.com/webtables')
            web_table_page.open()
            new_person = web_table_page.add_new_person()
            table_person = web_table_page.check_new_added_person()
            assert new_person in table_person
            time.sleep(1)

        @allure.title('Check Web Table Search Person')
        def test_web_table_search_person(self, driver):
            web_table_page = WebTablePage(driver, 'https://demoqa.com/webtables')
            web_table_page.open()
            key_word = web_table_page.add_new_person()[random.randint(0, 5)]
            time.sleep(1)
            web_table_page.search_some_person(key_word)
            time.sleep(1)
            table_result = web_table_page.check_search_person()
            assert key_word in table_result, "the person was not found in te table"

        @allure.title('Check Web Table Update info')
        def test_web_table_update_person_info(self, driver):
            web_table_page = WebTablePage(driver, 'https://demoqa.com/webtables')
            web_table_page.open()
            lastname = web_table_page.add_new_person()[1]
            web_table_page.search_some_person(lastname)
            age = web_table_page.update_person_info()

            row = web_table_page.check_search_person()
            assert age in row, "the person card has not been changed"

        @allure.title('Check Web Table delete person')
        def test_web_table_delete_person(self, driver):
            web_table_page = WebTablePage(driver, 'https://demoqa.com/webtables')
            web_table_page.open()
            email = web_table_page.add_new_person()[3]
            time.sleep(0.5)
            web_table_page.search_some_person(email)
            web_table_page.delete_person()
            text = web_table_page.check_deleted()
            assert text == "No rows found"

        @allure.title('Check Web Table Change count row')
        def test_web_table_change_count_row(self, driver):
            web_table_page = WebTablePage(driver, 'https://demoqa.com/webtables')
            web_table_page.open()
            count = web_table_page.select_up_to_some_rows()
            assert count == [5, 10, 20, 25, 50, 100], " the number of rows in the table has not been changed incorrectly"

    @allure.feature("ButtonsPage")
    class TestButtonsPage:

        @allure.title('Check Different click on the buttons')
        def test_different_click_on_the_buttons(self, driver):
            button_page = ButtonsPage(driver, 'https://demoqa.com/buttons')
            button_page.open()
            double = button_page.click_on_different_button("double")
            right = button_page.click_on_different_button("right")
            click = button_page.click_on_different_button("click")
            assert double == "You have done a double click", "The double click was not pressed"
            assert right == "You have done a right click", "The right click was not pressed"
            assert click == "You have done a dynamic click", "The dynamic click was not pressed"

    @allure.feature("LinkPage")
    class TestLinkPage:

        @allure.title('Check Check link')
        def test_check_link(self, driver):
            links_page = LinksPage(driver, 'https://demoqa.com/links')
            links_page.open()
            href_link, current_url = links_page.check_new_tab_simple_link()
            print(href_link)
            print(current_url)

        @allure.title('Check Broken Link')
        def test_broken_link(self, driver):
            links_page = LinksPage(driver, 'https://demoqa.com/links')
            links_page.open()
            response_code = links_page.check_broken_link('https://demoqa.com/bad-request')
            assert response_code == 400

    @allure.feature("UploadAndDownload")
    class TestUploadAndDownload:

        @allure.title('Check Upload file')
        def test_upload_file(self, driver):
            upload_download_page = UploadAndDownloadPage(driver, 'https://demoqa.com/upload-download')
            upload_download_page.open()
            file_name, result = upload_download_page.upload_file()
            assert file_name == result, "incorrect File Name or Path"

        @allure.title('Check download file')
        def test_download_file(self, driver):
            upload_download_page = UploadAndDownloadPage(driver, 'https://demoqa.com/upload-download')
            upload_download_page.open()
            check = upload_download_page.download_file()
            assert check is True, "File has not been downloaded"

    @allure.feature("DynamicProperties")
    class TestDynamicProperties:

        @allure.title('Check enable button')
        def test_enable_button(self, driver):
            dynamic_properties = DynamicPropertiesPage(driver, 'https://demoqa.com/dynamic-properties')
            dynamic_properties.open()
            dynamic_properties.check_enable_button()
            enable = dynamic_properties.check_appear_button()
            assert enable is True, "Button did not enable after 5 second"

        @allure.title('Check dynamic properties')
        def test_dynamic_properties(self, driver):
            dynamic_properties = DynamicPropertiesPage(driver, 'https://demoqa.com/dynamic-properties')
            dynamic_properties.open()
            color_before, color_after = dynamic_properties.check_changed_of_color()
            assert color_after != color_before, "Colors has not been changed"

        @allure.title('Check appear button')
        def test_appear_button(self, driver):
            dynamic_properties = DynamicPropertiesPage(driver, 'https://demoqa.com/dynamic-properties')
            dynamic_properties.open()
            appear = dynamic_properties.check_appear_button()
            assert appear is True, "Button did not appear after 5 second"

