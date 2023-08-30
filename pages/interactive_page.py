import random

from pages.base_page import BasePage
from locators.interactive_page_locators import SortablePageLocators, SelectablePageLocators, ResizablePageLocators, DroppablePageLocators
import time


class SortablePage(BasePage):

    def get_sortable_items(self, elements):
        item_list = self.elements_are_visible(elements)
        return [item.text for item in item_list]

    def change_list_order(self):
        self.element_is_visible(SortablePageLocators.TAB_LIST).click()
        order_before = self.get_sortable_items(SortablePageLocators.LIST_ITEM)
        item_list = random.sample(self.elements_are_visible(SortablePageLocators.LIST_ITEM), k=2)
        item_what = item_list[0]
        item_where = item_list[1]
        self.action_drag_and_drop_to_element(item_what, item_where)
        order_after = self.get_sortable_items(SortablePageLocators.LIST_ITEM)
        return order_before, order_after

    def change_grid_order(self):
        self.element_is_visible(SortablePageLocators.TAB_GRID).click()
        order_before = self.get_sortable_items(SortablePageLocators.GRID_LIST)
        item_list = random.sample(self.elements_are_visible(SortablePageLocators.GRID_LIST), k=2)
        item_what = item_list[0]
        item_where = item_list[1]
        self.action_drag_and_drop_to_element(item_what, item_where)
        order_after = self.get_sortable_items(SortablePageLocators.GRID_LIST)
        return order_before, order_after


class SelectablePage(BasePage):

    def click_selectable_item(self, elements):
        item_list = self.elements_are_visible(elements)
        random.sample(item_list, k=1)[0].click()

    def select_list_item(self):
        self.element_is_visible(SelectablePageLocators.TAB_LIST).click()
        self.click_selectable_item(SelectablePageLocators.LIST_ITEM)
        active_element = self.element_is_visible(SelectablePageLocators.LIST_ITEM_ACTIVE)
        return active_element.text

    def select_grid_item(self):
        self.element_is_visible(SelectablePageLocators.TAB_GRID).click()
        self.click_selectable_item(SelectablePageLocators.GRID_ITEM)
        active_element = self.element_is_visible(SelectablePageLocators.GRID_ITEM_ACTIVE)
        return active_element.text


class ResizablePage(BasePage):

    def get_px_from_width_height(self, value_of_size):
        width = value_of_size.split(';')[0].split(':')[1].replace(' ', '')
        height = value_of_size.split(';')[1].split(':')[1].replace(' ', '')
        return width, height

    def get_max_min_size(self, element):
        size = self.element_is_present(element)
        size_value = size.get_attribute('style')
        return size_value

    def change_size_resizable_box(self):
        self.action_drag_and_drop_by_offset(self.element_is_present(ResizablePageLocators.RESIZABLE_BOX_HANDLE), 400, 200)
        max_size = self.get_px_from_width_height(self.get_max_min_size(ResizablePageLocators.RESIZABLE_BOX))
        self.action_drag_and_drop_by_offset(self.element_is_present(ResizablePageLocators.RESIZABLE_BOX_HANDLE), -400, -200)
        min_size = self.get_px_from_width_height(self.get_max_min_size(ResizablePageLocators.RESIZABLE_BOX))
        return max_size, min_size

    def change_size_resizable(self):
        self.action_drag_and_drop_by_offset(self.element_is_present(ResizablePageLocators.RESIZABLE_HANDLE),
                                            random.randint(1, 300), random.randint(1, 300))
        max_size = self.get_px_from_width_height(self.get_max_min_size(ResizablePageLocators.RESIZABLE))
        self.action_drag_and_drop_by_offset(self.element_is_present(ResizablePageLocators.RESIZABLE_HANDLE),
                                            random.randint(-200, -1), random.randint(-200, -1))
        min_size = self.get_px_from_width_height(self.get_max_min_size(ResizablePageLocators.RESIZABLE))
        return max_size, min_size


class DroppablePage(BasePage):

    def drop_simple(self):
        self.element_is_visible(DroppablePageLocators.SIMPLE_TAB).click()
        drag_div = self.element_is_visible(DroppablePageLocators.DRAG_ME_SIMPLE)
        drop_div = self.element_is_visible(DroppablePageLocators.DROP_HERE_SIMPLE)
        self.action_drag_and_drop_to_element(drag_div, drop_div)
        return drop_div.text

    def drop_accept(self, div):
        self.element_is_visible(DroppablePageLocators.ACCEPT_TAB).click()
        divs = {"acceptable": DroppablePageLocators.ACCEPTABLE,
                "not_acceptable_div": DroppablePageLocators.NOT_ACCEPTABLE}
        drop_div = self.element_is_visible(DroppablePageLocators.DROP_HERE_ACCEPT)
        self.action_drag_and_drop_to_element(self.element_is_visible(divs[div]), drop_div)
        return drop_div.text

    def drop_prevent(self, drop):
        self.element_is_visible(DroppablePageLocators.PREVENT_TAB).click()
        drag_div = self.element_is_visible(DroppablePageLocators.DRAG_ME_PREVENT)
        drops = {"outer_droppable_top": DroppablePageLocators.NOT_GREEDY_DROP_BOX_TEXT,
                 "inner_droppable_top": DroppablePageLocators.NOT_GREEDY_INNER_BOX,
                 "outer_droppable_bot": DroppablePageLocators.GREEDY_DROP_BOX_TEXT,
                 "inner_droppable_bot": DroppablePageLocators.GREEDY_INNER_BOX}
        self.action_drag_and_drop_to_element(drag_div, self.element_is_visible(drops[drop]))
        drop_text = self.element_is_visible(drops[drop])
        return drop_text.text

    def drop_will_revert(self):
        self.element_is_visible(DroppablePageLocators.REVERT_TAB).click()
        will_revert = self.element_is_visible(DroppablePageLocators.WILL_REVERT)
        drop_div = self.element_is_visible(DroppablePageLocators.DROP_HERE_REVERT)
        self.action_drag_and_drop_to_element(will_revert, drop_div)
        position_after_move = will_revert.get_attribute('style')
        time.sleep(1)
        position_after_revert = will_revert.get_attribute('style')
        return position_after_move, position_after_revert

