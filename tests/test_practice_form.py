import time
import random
from pages.practice_form_page import PracticeFormPage


class TestForm:
    class TestFormPage:

        def test_form(self, driver):
            form_page = PracticeFormPage(driver, "https://demoqa.com/automation-practice-form")
            form_page.open()
            person_info, gender_name, hobbies, birth, file_name, subject, state_text, city_text\
                = form_page.fill_form_fields()
            result = form_page.get_form_result()

            assert person_info.firstname + " " + person_info.lastname == result[0]
            assert person_info.email == result[1]
            assert gender_name == result[2]
            #assert person_info.mobile == result[3]
            assert birth == result[4].replace(',', ' ').replace('e', '')
            assert subject == result[5]
            assert hobbies == result[6]
            assert file_name == result[7]
            assert person_info.current_address.replace('\n', '') == result[8]
            assert state_text + " " + city_text == result[9]

