﻿from .base_page import BasePage
from .locators import LoginPageLocators

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert 'login' in self.browser.current_url, "URL is not login"        
# реализуйте проверку на корректный url адрес
        assert True

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.login_form), "Login link is not presented"           
# реализуйте проверку, что есть форма логина
        assert True

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.register_form), "Login link is not presented"   
# реализуйте проверку, что есть форма регистрации на странице
        assert True