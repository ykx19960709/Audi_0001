from Base.base import Base

# 创建短信页面类,继承Base类
from Page.pageManagement import PageManagement


class Note(Base):
    def __init__(self,driver):
        Base.__init__(self,driver)
    # 点击新建短信按钮
    def click_new_note(self):
        self.click_methods(PageManagement.new_button)

