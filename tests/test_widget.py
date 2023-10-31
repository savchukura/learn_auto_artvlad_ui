import time
import allure
from pages.widget_page import AccordianPage, AutoCompletePage, DatePickerPage, SliderPage, ProgressBarPage, TabsPage, ToolTipsPage, MenuPage


@allure.suite("Widgets")
class TestWidgets:

    @allure.feature("Accordian Page")
    class TestAccordianPage:

        @allure.title('Check accordian')
        def test_accordian(self, driver):
            accordian_page = AccordianPage(driver, "https://demoqa.com/accordian")
            accordian_page.open()
            first_title, first_content = accordian_page.check_accordian('first')
            second_title, second_content = accordian_page.check_accordian('second')
            third_title, third_content = accordian_page.check_accordian('third')
            assert first_title == "What is Lorem Ipsum?" and first_content > 0
            assert second_title == "Where does it come from?" and second_content > 0
            assert third_title == "Why do we use it?" and third_content > 0

    @allure.feature("Auto complete Page")
    class TestAutoCompletePage:

        @allure.title('Check Fill multi autocomplete')
        def test_fill_multi_autocomplete(self, driver):
            autocomplete_page = AutoCompletePage(driver, "https://demoqa.com/auto-complete")
            autocomplete_page.open()
            colors = autocomplete_page.fill_input_multi()
            colors_result = autocomplete_page.check_color_in_multi()
            assert colors == colors_result

        @allure.title('Check remove value from multi')
        def test_remove_value_from_multi(self, driver):
            autocomplete_page = AutoCompletePage(driver, "https://demoqa.com/auto-complete")
            autocomplete_page.open()
            autocomplete_page.fill_input_multi()

            count_value_before, count_value_after = autocomplete_page.remove_value_from_multi()
            assert count_value_before != count_value_after

        @allure.title('Check fill single auto complete')
        def test_fill_single_auto_complete(self, driver):
            autocomplete_page = AutoCompletePage(driver, "https://demoqa.com/auto-complete")
            autocomplete_page.open()
            color = autocomplete_page.fill_input_single()
            color_result = autocomplete_page.check_color_in_single()
            assert color == color_result

    @allure.feature("Auto Date picker Page")
    class TestDatePickerPage:

        @allure.title('Check change data')
        def test_change_data(self, driver):
            date_picker_page = DatePickerPage(driver, "https://demoqa.com/date-picker")
            date_picker_page.open()
            value_date_before, value_date_after = date_picker_page.select_date()
            assert value_date_before != value_date_after, "date doesn't change"

        @allure.title('Check change date and time')
        def test_change_date_and_time(self, driver):
            date_picker_page = DatePickerPage(driver, "https://demoqa.com/date-picker")
            date_picker_page.open()
            value_date_before, value_date_after = date_picker_page.select_date_and_time()
            assert value_date_before != value_date_after, "date doesn't change"

    @allure.feature("Auto Slider Page")
    class TestSliderPage:

        @allure.title('Check slider')
        def test_slider(self, driver):
            slider = SliderPage(driver, 'https://demoqa.com/slider')
            slider.open()
            before, after = slider.change_slider_value()
            assert before != after, 'slider valou has not been change'

    @allure.feature("Auto Progress bar Page")
    class TestProgresBarPage:

        @allure.title('Check progress bar')
        def test_progress_bar(self, driver):
            progres_bar = ProgressBarPage(driver, 'https://demoqa.com/progress-bar')
            progres_bar.open()
            before, after = progres_bar.change_progress_bar_value()
            assert before != after, 'the progress bar value has not been changed'

    @allure.feature("Auto Tabs Page")
    class TestTabsPage:

        @allure.title('Check tabs')
        def test_tabs(self, driver):
            tabs = TabsPage(driver, "https://demoqa.com/tabs")
            tabs.open()
            what_button, what_content = tabs.check_tabs('what')
            origin_button, origin_content = tabs.check_tabs('origin')
            use_button, use_content = tabs.check_tabs('use')

            assert what_button == 'What' and what_content != 0
            assert origin_button == 'Origin' and origin_content != 0
            assert use_button == 'Use' and use_content != 0

    @allure.feature("Tool tips page")
    class TestToolTipsPage:

        @allure.title('Check tool tips')
        def test_tool_tips(self, driver):
            tool_tips_page = ToolTipsPage(driver, "https://demoqa.com/tool-tips")
            tool_tips_page.open()
            button_text, field_text, contrary_text, section_text = tool_tips_page.check_tool_tips()
            assert button_text == "You hovered over the Button"
            assert field_text == "You hovered over the text field"
            assert contrary_text == 'You hovered over the Contrary'
            assert section_text == 'You hovered over the 1.10.32'

            # for this test you must use not only Elements in dev tools, Actually you need use "Source in dev tools
            # for stop activiti on page and catch hover text

    @allure.feature("Menu page")
    class TestMenuPage:

        @allure.title('Check menu items')
        def test_menu_items(self, driver):
            menu_page = MenuPage(driver, "https://demoqa.com/menu")
            menu_page.open()
            data = menu_page.check_menu()
            assert data == ['Main Item 1', 'Main Item 2', 'Sub Item', 'Sub Item', 'SUB SUB LIST »',
                            'Sub Sub Item 1', 'Sub Sub Item 2', 'Main Item 3']
