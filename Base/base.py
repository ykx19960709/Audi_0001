from selenium.webdriver.support.wait import WebDriverWait


class Base:
    # 传入driver
    def __init__(self, driver):
        self.driver = driver

    # 单个元素定位方法返回
    def find_one_methods(self, loc, timeout=5, poll=1):
        return WebDriverWait(self.driver, timeout, poll).until(lambda x: x.find_element(*loc))

    # 多个元素定位返回
    def find_multiple_methods(self, loc, timeout=5, poll=1):
        return WebDriverWait(self.driver, timeout, poll).until(lambda x: x.find_elements(*loc))

    # 点击方法
    def click_methods(self, loc, timeout=5, poll=1):
        self.find_one_methods(loc, timeout, poll).click()

    # 输入方法
    def input_methods(self, loc, text, timeout=5, poll=1):
        # 定位,并实例化
        input_text = self.find_one_methods(loc, timeout, poll)
        # 清空
        input_text.clear()
        # 输入内容
        input_text.send_keys(text)
