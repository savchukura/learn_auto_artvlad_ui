import time
import allure
from pages.interactive_page import SortablePage, SelectablePage, ResizablePage, DroppablePage
#from conftest import *


@allure.suite("Interactions")
class TestInteractions:

    @allure.feature("Sortable page")
    class TestSortablePage:

        @allure.title('Check Sortable list')
        def test_sortable_list(self, driver):
            sortable_page = SortablePage(driver, "https://demoqa.com/sortable")
            sortable_page.open()
            before, after = sortable_page.change_list_order()
            assert before != after, ""

        @allure.title('Check Sortable grid')
        def test_sortable_grid(self, driver):
            sortable_page = SortablePage(driver, "https://demoqa.com/sortable")
            sortable_page.open()
            before, after = sortable_page.change_grid_order()
            assert before != after, "s"

    @allure.feature("Selectable page")
    class TestSelectablePage:

        @allure.title('Check Selectable')
        def test_selectable(self, driver):
            selectable_page = SelectablePage(driver, "https://demoqa.com/selectable")
            selectable_page.open()
            item_list = selectable_page.select_list_item()
            item_grid = selectable_page.select_grid_item()
            assert len(item_list) > 0, "s"
            assert len(item_grid) > 0, "s"

    @allure.feature("Resizable page")
    class TestResizablePage:

        @allure.title('Check resizable')
        def test_resizable(self, driver):
            resizable_page = ResizablePage(driver, "https://demoqa.com/resizable")
            resizable_page.open()
            max_box, min_box = resizable_page.change_size_resizable_box()
            max_resize, min_resize = resizable_page.change_size_resizable()
            print(max_box, min_box)
            print(max_resize, min_resize)
            assert ('500px', '300px') == max_box
            assert ('150px', '150px') == min_box

    @allure.feature("Droppable page")
    class TestDroppablePage:

        @allure.title('Check simple droppable')
        def test_simple_droppable(self, driver):
            droppable_page = DroppablePage(driver, "https://demoqa.com/droppable")
            droppable_page.open()
            text = droppable_page.drop_simple()
            assert text == "Dropped!"

        @allure.title('Check accept droppable')
        def test_accept_droppable(self, driver):
            droppable_page = DroppablePage(driver, "https://demoqa.com/droppable")
            droppable_page.open()
            text = droppable_page.drop_accept("acceptable")
            assert text == "Dropped!"

        @allure.title('Check not accept droppable')
        def test_not_accept_droppable(self, driver):
            droppable_page = DroppablePage(driver, "https://demoqa.com/droppable")
            droppable_page.open()
            text = droppable_page.drop_accept("not_acceptable_div")
            assert text == "Drop here"

        @allure.title('Check propogation outer droppable top')
        def test_propogation_outer_droppable_top(self, driver):
            droppable_page = DroppablePage(driver, "https://demoqa.com/droppable")
            droppable_page.open()
            text = droppable_page.drop_prevent("outer_droppable_top")
            assert text == "Dropped!"

        @allure.title('Check propogation inner droppable top')
        def test_propogation_inner_droppable_top(self, driver):
            droppable_page = DroppablePage(driver, "https://demoqa.com/droppable")
            droppable_page.open()
            text = droppable_page.drop_prevent("inner_droppable_top")
            assert text == "Dropped!"

        @allure.title('Check propogation outer droppable top')
        def test_propogation_outer_droppable_bot(self, driver):
            droppable_page = DroppablePage(driver, "https://demoqa.com/droppable")
            droppable_page.open()
            text = droppable_page.drop_prevent("outer_droppable_bot")
            assert text == "Dropped!"

        @allure.title('Check propogation inner droppable bot')
        def test_propogation_inner_droppable_bot(self, driver):
            droppable_page = DroppablePage(driver, "https://demoqa.com/droppable")
            droppable_page.open()
            text = droppable_page.drop_prevent("inner_droppable_bot")
            assert text == "Dropped!"

        @allure.title('Check draggable droppable')
        def test_revert_draggable_droppable(self, driver):
            droppable_page = DroppablePage(driver, "https://demoqa.com/droppable")
            droppable_page.open()
            will_after_move, will_after_revert = droppable_page.drop_will_revert()
            print(will_after_move)
            print(will_after_revert)
