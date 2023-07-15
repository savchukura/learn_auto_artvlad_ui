import random
import time

from selenium.common import TimeoutException
from selenium.webdriver import Keys
from selenium.webdriver.support.select import Select

from generator.generator import generated_color, generated_date
from pages.base_page import BasePage
from locators.widget_page_locators import AccordianPageLocators, AutoCompletePageLocators, DatePickerPageLocators, SliderPageLocators, ProgressBarPageLocators


class AccordianPage(BasePage):

    def check_accordian(self, accordian_num):
        accordian = {"first":
                        {'title': AccordianPageLocators.SECTION_FIRST,
                         'content': AccordianPageLocators.SECTION_CONTENT_FIRST},
                     "second":
                         {'title': AccordianPageLocators.SECTION_SECOND,
                          'content': AccordianPageLocators.SECTION_CONTENT_SECOND},
                     "third":
                         {'title': AccordianPageLocators.SECTION_THIRD,
                          'content': AccordianPageLocators.SECTION_CONTENT_THIRD}
                    }
        section_title = self.element_is_present(accordian[accordian_num]['title'])
        section_title.click()
        try:

            section_content = self.element_is_visible(accordian[accordian_num]['content']).text
        except TimeoutException:
            section_title.click()
            section_content = self.element_is_visible(accordian[accordian_num]['content']).text
        return [section_title.text, len(section_content)]


class AutoCompletePage(BasePage):

    def fill_input_multi(self):
        colors = random.sample(next(generated_color()).color_name, k=random.randint(2, 5))
        for color in colors:
            input_multi = self.element_is_visible(AutoCompletePageLocators.MULTI_INPUT)
            input_multi.send_keys(color)
            input_multi.send_keys(Keys.ENTER)
        return colors

    def remove_value_from_multi(self):
        count_value_before = len(self.elements_are_present(AutoCompletePageLocators.MULTI_VALUE))
        remove_button_list = (self.elements_are_visible(AutoCompletePageLocators.MULTI_VALUE_REMOVE))
        for value in remove_button_list:
            value.click()
            break
        count_value_after = len(self.elements_are_present(AutoCompletePageLocators.MULTI_VALUE))
        return count_value_before, count_value_after

    def check_color_in_multi(self):
        color_list = self.elements_are_present(AutoCompletePageLocators.MULTI_VALUE)
        colors = []
        for color in color_list:
            colors.append(color.text)
        return colors

    def fill_input_single(self):
        color = random.sample(next(generated_color()).color_name, k=1)
        input_single = self.element_is_clickable(AutoCompletePageLocators.SINGLE_INPUT)
        input_single.send_keys(color)
        input_single.send_keys(Keys.ENTER)
        return color[0]

    def check_color_in_single(self):
        color = self.element_is_visible(AutoCompletePageLocators.SINGLE_CONTAINER)
        return color.text


class DatePickerPage(BasePage):

    def select_date(self):
        date = next(generated_date())
        input_date = self.element_is_visible(DatePickerPageLocators.DATE_INPUT)
        value_date_before = input_date.get_attribute('value')
        input_date.click()
        self.set_date_by_text(DatePickerPageLocators.DATE_SELECT_MONTH, date.month)
        self.set_date_by_text(DatePickerPageLocators.DATE_SELECT_YEAR, date.year)
        self.set_date_item_from_list(DatePickerPageLocators.DATE_SELECT_DAY_LIST, date.day)
        value_date_after = input_date.get_attribute('value')
        return value_date_before, value_date_after

    def set_date_by_text(self, element, value):
        select = Select(self.element_is_present(element))
        select.select_by_visible_text(value)

    def set_date_item_from_list(self, elements, value):
        item_list = self.elements_are_present(elements)
        for item in item_list:
            if item.text == value:
                item.click()
                break

    def select_date_and_time(self):
        date = next(generated_date())
        input_date = self.element_is_visible(DatePickerPageLocators.DATE_AND_TIME_INPUT)
        value_date_before = input_date.get_attribute('value')
        input_date.click()
        self.element_is_visible(DatePickerPageLocators.DATE_AND_TIME_MONTH).click()
        self.set_date_item_from_list(DatePickerPageLocators.DATE_AND_TIME_MONTH_LIST, date.month)
        self.element_is_visible(DatePickerPageLocators.DATE_AND_TIME_YEAR).click()
        self.set_date_item_from_list(DatePickerPageLocators.DATE_AND_TIME_YEAR_LIST, "2023")
        self.set_date_item_from_list(DatePickerPageLocators.DATE_SELECT_DAY_LIST, date.day)
        self.set_date_item_from_list(DatePickerPageLocators.DATE_AND_TIME_TIME_LIST, date.time)
        value_date_after = input_date.get_attribute('value')
        return value_date_before, value_date_after


class SliderPage(BasePage):

    def change_slider_value(self):
        value_before = self.element_is_visible(SliderPageLocators.SLIDER_VALUE).get_attribute('value')
        slider_input = self.element_is_visible(SliderPageLocators.INPUT_SLIDER)
        self.action_drag_and_drop_by_offset(slider_input, -400, 0)
        value_after = self.element_is_visible(SliderPageLocators.SLIDER_VALUE).get_attribute('value')

        return value_before, value_after


class ProgressBarPage(BasePage):

    def change_progress_bar_value(self):
        value_before = self.element_is_present(ProgressBarPageLocators.PROGRESS_BAR_VALUE).text
        progres_bar_button = self.element_is_visible(ProgressBarPageLocators.PROGRESS_BAR_BUTTON)
        progres_bar_button.click()
        time.sleep(random.randint(2, 5))
        progres_bar_button.click()
        value_after = self.element_is_present(ProgressBarPageLocators.PROGRESS_BAR_VALUE).text
        return value_before, value_after

