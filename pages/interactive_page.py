import random

from pages.base_page import BasePage
from locators.interactive_page_locators import SortablePageLocators

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
