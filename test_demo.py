from selenium import webdriver


options = webdriver.ChromeOptions()
driver = webdriver.Chrome(options=options)
options.add_argument("--start-maximized")

driver.get(url="https://the-internet.herokuapp.com/abtest")
def test_demo1():
    assert 1 == 1


def test_demo2():
    assert 2 == 2
