from pages.elements_page import TextBoxPage
from pages.elements_page import CheckBoxPage
import time


class TestElements:
    class TestTextBox:
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

    class TestCheckBox:

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

