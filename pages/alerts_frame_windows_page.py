from pages.base_page import BasePage
from locators.alerts_frame_windows_locators import BrowserWindowsPageLocators


class BrowserWindowsPage(BasePage):

    def check_opened_new_tab(self):
        self.element_is_visible(BrowserWindowsPageLocators.NEW_TAB_BUTTON).click()
        self.switch_to_another_window(1)
        text_title = self.element_is_present(BrowserWindowsPageLocators.TITLE_NEW).text
        return text_title

    def check_opened_new_window(self):
        self.element_is_visible(BrowserWindowsPageLocators.NEW_WINDOW_BUTTON).click()
        self.switch_to_another_window(1)
        text_title = self.element_is_present(BrowserWindowsPageLocators.TITLE_NEW).text
        return text_title

