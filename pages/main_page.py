import random
import time
from selenium.webdriver.support import expected_conditions as EC
import allure
from locators.main_pages_locators import MainPage_locators


class MainPage:

    def __init__(self, driver):
        self.driver = driver

    @allure.step("Проверка активности ссылки «Личный Кабинет» в панели навигации")
    def check_click_cabinet(self):
        self.driver.find_element(*MainPage_locators.cabinet).is_displayed()

    @allure.step("Нажатие на ссылку «Личный Кабинет» в панели навигации")
    def click_cabinet(self):  # Личный кабинет
        self.driver.find_element(*MainPage_locators.cabinet).click()
        assert self.driver.find_element(*MainPage_locators.assert_page_loc), 'Ожидается кнопка войти'

    @allure.step("Проверка активности кнопки «Войти в аккаунт»")
    def check_click_cabinet_btn(self):
        self.driver.find_element(*MainPage_locators.btn_account).is_displayed()

    @allure.step("Нажатие на кнопку ""Войти в аккаунт""")
    def click_cabinet_btn(self):  # Личный кабинет через кнопку на главном экране
        self.driver.find_element(*MainPage_locators.btn_account).click()
        assert self.driver.find_element(*MainPage_locators.assert_page_loc), 'Ожидается кнопка войти'

    @allure.step("Рандомный выбор булки")
    def choosing_loaf(self): # Нажатие на Рандомную булку
        element = self.driver.find_elements(*MainPage_locators.choosing_loaf)
        random_loaf = random.choice(element)
        random_loaf.click()
        assert self.driver.find_element(*MainPage_locators.popup).is_displayed()

    @allure.step("Рандомный выбор булки")
    def choosing_sauce(self):  # Нажатие на Рандомную булку
        element = self.driver.find_elements(*MainPage_locators.choosing_sauce)
        random_loaf = random.choice(element)
        random_loaf.click()
        assert self.driver.find_element(*MainPage_locators.popup).is_displayed()

    @allure.step("Рандомный выбор булки")
    def choosing_filling(self):  # Нажатие на Рандомную булку
        element = self.driver.find_elements(*MainPage_locators.choosing_filling)
        random_loaf = random.choice(element)
        random_loaf.click()
        assert self.driver.find_element(*MainPage_locators.popup).is_displayed()

    @allure.step("Закрыть поп ап")
    def popup_exit(self): # Нажатие на Рандомную булку
        self.driver.find_element(*MainPage_locators.exit_popup).click()
        time.sleep(1)
        assert  self.driver.find_element(*MainPage_locators.popup).is_displayed() == False
