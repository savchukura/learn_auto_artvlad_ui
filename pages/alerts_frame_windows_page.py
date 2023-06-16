import random

from selenium.common import UnexpectedAlertPresentException
import time

from pages.base_page import BasePage
from locators.alerts_frame_windows_locators import BrowserWindowsPageLocators, AlertsPageLocators


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


class AlertsPage(BasePage):

    def check_see_alert(self):
        self.element_is_visible(AlertsPageLocators.SEE_ALERT_BUTTON).click()
        alert_window = self.driver.switch_to.alert
        return alert_window.text

    def check_alert_appear_5_sec(self):
        self.element_is_visible(AlertsPageLocators.APPEAR_ALERT_AFTER_5_SEC_BUTTON).click()
        time.sleep(6)
        try:
            alert_window = self.driver.switch_to.alert
            return alert_window.text
        except UnexpectedAlertPresentException:
            alert_window = self.driver.switch_to.alert
            return alert_window.text

    def check_confirm_alert(self):
        self.element_is_visible(AlertsPageLocators.CONFIRM_BOX_ALERT_BUTTON).click()
        alert_window = self.driver.switch_to.alert
        alert_window.accept()
        text_result = self.element_is_present(AlertsPageLocators.CONFIRM_RESULT).text
        return text_result

    def check_prompt_alert(self):
        text = f'autotest{random.randint(0,999)}'
        self.element_is_visible(AlertsPageLocators.PROMPT_BOX_ALERT_BUTTON).click()
        alert_window = self.driver.switch_to.alert
        alert_window.send_keys(text)
        alert_window.accept()
        text_result = self.element_is_present(AlertsPageLocators.PROMPT_RESULT).text
        return text, text_result
