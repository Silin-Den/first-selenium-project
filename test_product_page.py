
import pytest
import time

from pages.product_page import ProductPage
from pages.basket_page import BasketPage
from pages.base_page import BasePage
from pages.login_page import LoginPage

# link = " http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"

@pytest.mark.new
class TestUserAddToBasketFromProductPage():
     
    @pytest.fixture(scope="function",autouse=True)
    def setup(self, browser):           
        email = str(time.time()) + "@fakemail.org"
        password = str(time.time()).split('.')[0]
                    
        page = ProductPage(browser, link)
        page.open()
        page.go_to_login_page()
        login = LoginPage(browser, browser.current_url)
        login.register_new_user(email,password)
        login.should_be_authorized_user()            
 
    
    def test_user_cant_see_success_message_before_adding_product_to_basket(self,browser):
        page = ProductPage(browser,link)
        page.open()
        page.should_not_be_success_message()


#     @pytest.mark.xfail    
    def  test_user_can_add_product_to_basket(self,browser):

        page = ProductPage(browser,link)
        page.open()
        page.should_not_be_success_message()
        page.add_product_to_basket()
        page.should_be_success_message()
        @pytest.mark.xfail
        page.success_message_should_disappear()
          
            
def test_guest_should_see_login_link_on_product_page(browser):

    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()
    
def test_guest_can_go_to_login_page_from_product_page(browser):

    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()


@pytest.mark.basket        
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    
    page = ProductPage(browser, link)
    page.open()
    page.go_to_basket()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_not_be_goods_in_basket()
    basket_page.should_be_text_about_basket() 
    
