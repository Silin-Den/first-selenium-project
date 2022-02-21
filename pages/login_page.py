
from .base_page import BasePage
from .locators import LoginPageLocators

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
