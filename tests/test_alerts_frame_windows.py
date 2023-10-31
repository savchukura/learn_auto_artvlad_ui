from pages.alerts_frame_windows_page import BrowserWindowsPage, AlertsPage, FramesPage, NestedFramesPage, \
    ModalDialogsPage
import allure


@allure.suite("AlertsFrameWindow")
class TestAlertsFrameWindow:
    @allure.feature("BrowserWindows")
    class TestBrowserWindows:

        @allure.title('New tab')
        def test_new_tab(self, driver):
            new_tab_page = BrowserWindowsPage(driver, "https://demoqa.com/browser-windows")
            new_tab_page.open()
            new_tab = new_tab_page.check_opened_new_tab()
            assert new_tab == "This is a sample page", "invalid text"

        @allure.title('New window')
        def test_new_window(self, driver):
            new_window_page = BrowserWindowsPage(driver, "https://demoqa.com/browser-windows")
            new_window_page.open()
            new_tab = new_window_page.check_opened_new_window()
            assert new_tab == "This is a sample page", "invalid text"

    @allure.feature("AlertsPage")
    class TestAlertsPage:

        @allure.title('See alert')
        def test_see_alert(self, driver):
            alert_page = AlertsPage(driver, "https://demoqa.com/alerts")
            alert_page.open()
            alert_window = alert_page.check_see_alert()
            assert alert_window == 'You clicked a button', "Alert did not show up"

        @allure.title('Alert appear 5 sec')
        def test_alert_appear_5_sec(self, driver):
            alert_page = AlertsPage(driver, "https://demoqa.com/alerts")
            alert_page.open()
            alert_window = alert_page.check_alert_appear_5_sec()
            assert alert_window == 'This alert appeared after 5 seconds', "Alert did not show up"

        @allure.title('Confirm alert')
        def test_confirm_alert(self, driver):
            alert_page = AlertsPage(driver, "https://demoqa.com/alerts")
            alert_page.open()
            alert_window = alert_page.check_confirm_alert()
            assert alert_window == 'You selected Ok', "Alert did not show up"

        @allure.title('Prompt alert')
        def test_prompt_alert(self, driver):
            alert_page = AlertsPage(driver, "https://demoqa.com/alerts")
            alert_page.open()
            text, alert_window = alert_page.check_prompt_alert()
            assert alert_window == f'You entered {text}', "Alert did not show up"

    @allure.feature("Frames Page")
    class TestFramesPage:

        @allure.title('Frames')
        def test_frames(self, driver):
            frames_page = FramesPage(driver, "https://demoqa.com/frames")
            frames_page.open()
            result_frame_one = frames_page.check_frame('frame1')
            result_frame_two = frames_page.check_frame('frame2')
            assert result_frame_one == ['500px', '350px', 'This is a sample page'], "the frame does not exist"
            assert result_frame_two == ['100px', '100px', 'This is a sample page'], "the frame does not exist"

    @allure.feature("Nested Frames Page")
    class TestNestedFramesPage:

        @allure.title('Nested Frames')
        def test_nested_frames(self, driver):
            nested_frames_page = NestedFramesPage(driver, "https://demoqa.com/nestedframes")
            nested_frames_page.open()
            parent_text, child_text = nested_frames_page.check_nested_frame()
            assert parent_text == "Parent frame", "incorrect text in Parent frame"
            assert child_text == "Child Iframe", "incorrect text in Child frame"

    @allure.feature("Modal Dialog Page")
    class TestModalDialogPage:

        @allure.title('Modal dialogs')
        def test_modal_dialogs(self, driver):
            modal_dialogs_page = ModalDialogsPage(driver, "https://demoqa.com/modal-dialogs")
            modal_dialogs_page.open()
            small, large = modal_dialogs_page.check_modal_dialogs()
            assert small[1] < large[1]
            assert small[0] == 'Small Modal'
            assert large[0] == 'Large Modal'

