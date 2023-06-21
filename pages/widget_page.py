from selenium.common import TimeoutException

from pages.base_page import BasePage
from locators.widget_page_locators import AccordianPageLocators


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