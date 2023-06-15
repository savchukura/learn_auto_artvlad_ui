from pages.alerts_frame_windows_page import BrowserWindowsPage


class TestAlertsFrameWindow:

    class TestBrowserWindows:

        def test_new_tab(self, driver):
            new_tab_page = BrowserWindowsPage(driver, "https://demoqa.com/browser-windows")
            new_tab_page.open()
            new_tab = new_tab_page.check_opened_new_tab()
            assert new_tab == "This is a sample page", "invalid text"

        def test_new_window(self, driver):
            new_window_page = BrowserWindowsPage(driver, "https://demoqa.com/browser-windows")
            new_window_page.open()
            new_tab = new_window_page.check_opened_new_window()
            assert new_tab == "This is a sample page", "invalid text"
