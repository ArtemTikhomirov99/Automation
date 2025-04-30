class MainPage_locators:
    cabinet = ["xpath", "//nav/a"]  # Личный кабинет
    btn_account = ["xpath", '//*[@id="root"]/div/main/section[2]/div/button']  # вход через кнопку
    assert_page_loc = ["xpath", "//button[text()='Войти']"]
    choosing_loaf = ["xpath", "//main/section[1]//ul[1]/a"]
    choosing_sauce = ["xpath", "//main/section[1]//ul[2]/a"]
    choosing_filling = ["xpath", "//main/section[1]//ul[3]/a"]
    popup = ["xpath", '//div/section[1]/div[1]']
    exit_popup = ["xpath", '//div/section[1]//button']