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
