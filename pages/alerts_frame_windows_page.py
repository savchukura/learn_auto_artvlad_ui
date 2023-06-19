import random

from selenium.common import UnexpectedAlertPresentException
import time

from pages.base_page import BasePage
from locators.alerts_frame_windows_locators import BrowserWindowsPageLocators, AlertsPageLocators, FramesPageLocators, NestedFramesPageLocators, ModalDialogsPageLocators


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


class FramesPage(BasePage):

    def check_frame(self, frame_num):
        if frame_num == "frame1":
            frame = self.element_is_present(FramesPageLocators.FIRST_FRAME)
            width = frame.get_attribute('width')
            height = frame.get_attribute('height')
            self.driver.switch_to.frame(frame)
            text = self.element_is_present(FramesPageLocators.TITLE_FRAME).text
            self.driver.switch_to.default_content()
            return [width, height, text]
        if frame_num == "frame2":
            frame = self.element_is_present(FramesPageLocators.SECOND_FRAME)
            width = frame.get_attribute('width')
            height = frame.get_attribute('height')
            self.driver.switch_to.frame(frame)
            text = self.element_is_present(FramesPageLocators.TITLE_FRAME).text
            self.driver.switch_to.default_content()
            return [width, height, text]


class NestedFramesPage(BasePage):

    def check_nested_frame(self):
        parent_frame = self.element_is_present(NestedFramesPageLocators.PARENT_FRAME)
        self.driver.switch_to.frame(parent_frame)
        parent_text = self.element_is_present(NestedFramesPageLocators.PARENT_TEXT).text
        child_frame = self.element_is_present(NestedFramesPageLocators.CHILD_FRAME)
        self.driver.switch_to.frame(child_frame)
        child_text = self.element_is_present(NestedFramesPageLocators.CHILD_TEXT).text
        return parent_text, child_text


class ModalDialogsPage(BasePage):

    def check_modal_dialogs(self):
        self.element_is_visible(ModalDialogsPageLocators.SMALL_MODAL_BUTTON).click()
        small_modal_title = self.element_is_visible(ModalDialogsPageLocators.SMALL_MODAL_TITLE).text
        small_modal_text = self.element_is_visible(ModalDialogsPageLocators.SMALL_MODAL_TEXT).text
        self.element_is_visible(ModalDialogsPageLocators.CLOSE_SMALL_MODAL_BUTTON).click()
        self.element_is_visible(ModalDialogsPageLocators.LARGE_MODAL_BUTTON).click()
        large_modal_title = self.element_is_visible(ModalDialogsPageLocators.LARGE_MODAL_TITLE).text
        large_modal_text = self.element_is_visible(ModalDialogsPageLocators.LARGE_MODAL_TEXT).text
        return [small_modal_title, len(small_modal_text)], [large_modal_title, len(large_modal_text)]






