from .pages.main_page import MainPage
from .pages.product_page import Page_Object
from selenium.common.exceptions import NoAlertPresentException

def test_guest_can_add_product_to_basket(browser):
    #link ="http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    link="http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    page = Page_Object(browser, link)   
    page.open()                     
    page.should_be_added_to_basket()
    page.solve_quiz_and_get_code()
    page.should_be_message()
    page.should_be_correct_basket()

def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link ="http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = Page_Object(browser, link)   
    page.open()
    page.should_be_added_to_basket()
    page.solve_quiz_and_get_code()
    page.should_not_be_success_message()

def test_guest_cant_see_success_message(browser):
    link ="http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = Page_Object(browser, link)   
    page.open()
    page.should_not_be_success_message()

def test_message_disappeared_after_adding_product_to_basket(browser):
    link ="http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = Page_Object(browser, link)   
    page.open()
    page.should_be_added_to_basket()
    page.solve_quiz_and_get_code()
    page.should_be_disappeared_element()

def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = Page_Object(browser, link)
    page.open()
    page.should_be_login_link()

def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = Page_Object(browser, link)
    page.open()
    page.go_to_login_page()
    
