
from selenium.webdriver.common.by import By
from .base_page import BasePage
from .locators import BasketPageLocators

class BasketPage(BasePage):
    
    def should_not_be_goods_in_basket(self):
        
        assert self.is_not_element_present(*BasketPageLocators.TOTAL_GOODS)," Basket is not empty!"
        print('Your code: Congratulations! Basket is empty..')
    
    def should_be_text_about_basket(self):
        
        assert self.is_element_present(*BasketPageLocators.TOTAL_GOODS_LABEL), "Empty title!" 
        print('Your code: Congratulations! Label in page..')
