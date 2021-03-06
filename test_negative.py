
import pytest
import time
from pages.product_page import ProductPage
from pages.basket_page import BasketPage

link = " http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"


class Test_Negative():
    @pytest.mark.xfail
    def test_guest_cant_see_success_message_after_adding_product_to_basket(self,browser):
        page = ProductPage(browser,link)
        page.open()
        page.add_product_to_basket()
        page.should_not_be_success_message()
        
    def test_guest_cant_see_success_message_before_adding_product_to_basket(self,browser):
        page = ProductPage(browser,link)
        page.open()
        page.should_not_be_success_message()
        
    @pytest.mark.xfail    
    def test_message_disappeared_after_adding_product_to_basket(self,browser):
        page = ProductPage(browser,link)
        page.open()
        page.add_product_to_basket()
        page.success_message_should_disappear()
