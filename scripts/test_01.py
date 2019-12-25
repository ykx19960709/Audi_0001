import pytest

from Base.element import Page
from Base.getDriver import get_android_driver


class TestNote:

    def setup_class(self):
        # 初始化driver
        self.driver = get_android_driver('com.android.mms','.ui.ConversationList')

        # 实例化统一入口类
        self.page_obj = Page(self.driver)
    def teardown_class(self):
        self.driver.quit()

    # 进入新建短信界面
    @pytest.fixture(scope="class",autouse=True)
    def goto_sendnote_page(self):
        # 点击新建短信按钮
        self.page_obj.get_note_page().click_new_note()
    @pytest.mark.parametrize("dh,dy",[["13512345678","sun"]])
    def test_sendnote(self,dh,dy):
        # 输入电话
        self.page_obj.get_sendnote_page().find_srk_01(dh)
        # 输入发送内容
        self.page_obj.get_sendnote_page().find_srk_02(dy)
        # 断言
        assert dy in self.page_obj.get_sendnote_page().get_result()

