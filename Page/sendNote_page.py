# 发送信息页面
from Base.base import Base
from Page.pageManagement import PageManagement


class SendNote(Base):
    def __init__(self,driver):
        Base.__init__(self,driver)
    def find_srk_01(self,text):
        # 接收人输入框
        self.input_methods(PageManagement.input_jsr,text)
        # 发送内容输入框
    def find_srk_02(self,text):
        self.input_methods(PageManagement.input_nr,text)
        # 发送按钮
        self.click_methods(PageManagement.send_button)
        # 定位页面所有元素
    def get_result(self):
        return [i.text for i in self.find_multiple_methods(PageManagement.get_note_summary_text_ids)]
