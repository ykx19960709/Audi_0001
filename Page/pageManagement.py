from selenium.webdriver.common.by import By


class PageManagement:
    # 短信页面
    # 新建按钮
    new_button = (By.ID,"com.android.mms:id/action_compose_new")


    # 新建短信页面
    # 接收人
    input_jsr = (By.ID,"com.android.mms:id/recipients_editor")
    # 输入内容框
    input_nr = (By.ID,"com.android.mms:id/embedded_text_editor")
    # 点击发送按钮
    send_button = (By.ID,"com.android.mms:id/send_button_sms")
    # 获取当前页面的所有summary信息
    get_note_summary_text_ids = (By.ID,"com.android.mms:id/text_view")
