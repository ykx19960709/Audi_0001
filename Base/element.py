# 统一入口类
from Page.note_page import Note
from Page.sendNote_page import SendNote


class Page:
    def __init__(self,driver):
        self.driver = driver
    # 返回短信页面实例化对象
    def get_note_page(self):
        return Note(self.driver)
    # 返回编辑短信页面实例化对象
    def get_sendnote_page(self):
        return SendNote(self.driver)