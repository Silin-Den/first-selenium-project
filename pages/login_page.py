
from .base_page import BasePage
from .locators import LoginPageLocators
import time

class LoginPage(BasePage):

    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):        
        assert "login" in self.browser.current_url, 'Incorrected URL (not inclusive substring "login").'

    def should_be_login_form(self):
        assert self.browser.find_element(*LoginPageLocators.LOGIN_FORM) ,'Up-s-s...Login form not found!'

    def should_be_register_form(self):
        assert self.browser.find_element(*LoginPageLocators.REGISTER_FORM),'Up-s-s...Register form not found!'
        
        
    def register_new_user(self,email,password): 

        reg_email = self.browser.find_element(*LoginPageLocators.EMAIL)
        reg_email.send_keys(email)
        
        reg_rswd = self.browser.find_element(*LoginPageLocators.PSWD1)
        reg_rswd.send_keys(password)
        
        reg_rswd2 = self.browser.find_element(*LoginPageLocators.PSWD2)
        reg_rswd2.send_keys(password)
        
        button = self.browser.find_element(*LoginPageLocators.SUBMIT)
        button.click()
