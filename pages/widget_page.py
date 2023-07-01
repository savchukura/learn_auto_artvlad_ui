import random

from selenium.common import TimeoutException
from selenium.webdriver import Keys

from generator.generator import generated_color
from pages.base_page import BasePage
from locators.widget_page_locators import AccordianPageLocators, AutoCompletePageLocators


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

