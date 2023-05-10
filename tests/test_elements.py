from pages.elements_page import TextBoxPage
import time


def test(driver):
    text_box_page = TextBoxPage(driver, "https://demoqa.com/text-box")
    text_box_page.open()
    full_name, email, current_address, permanent_address = text_box_page.fill_all_fields()
    output_name, output_email, output_current_address, output_permanent_address = text_box_page.check_filled_form()
    assert full_name == output_name, "full name incorrect"
    assert email == output_email, "email incorrect"
    assert current_address == output_current_address, "current_address incorrect"
    assert permanent_address == output_permanent_address, "permanent address incorrect"
    time.sleep(3)