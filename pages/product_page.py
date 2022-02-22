
from selenium.webdriver.common.by import By
from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):
    
    def add_product_to_basket(self):
        self.should_be_button()
        self.solve_quiz_and_get_code()
        self.should_be_equal_name()
        self.should_be_equal_price()
    
    def should_be_button(self): 
        
        button = self.browser.find_element(*ProductPageLocators.BASKET_BUTTON)
        button.click()
        print('Your code: Congratulations! Buttton presented!--> ')
    
    def should_be_equal_name(self):
        
        product_name  = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME)
        basket_name  = self.browser.find_element(*ProductPageLocators.BUSKET_PRODUCT_NAME)
        assert basket_name.text == product_name.text, 'not equal names!!'
        print('Your code: Congratulations! Couple name is equal! --> ')
        
    def should_be_equal_price(self):
        
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE)
        basket_price  = self.browser.find_element(*ProductPageLocators.BUSKET_PRODUCT_PRICE)
        assert basket_price.text == product_price.text, 'not equal prices!!'
        print('Your code: Congratulations! Couple price is equal! --> ')
        
    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
           "Success message is presented, but should not be" 
        print('Your code: Congratulations! Success message not presented! --> ')
        
    def should_be_success_message(self):
        assert self.is_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
           "Success message not presented, but should be!"  
        print('Your code: Congratulations! Success message presented! --> ')
        
    def success_message_should_disappear(self):
        assert False
        print('Your code: Congratulations! Success message disappeared! --> ')
