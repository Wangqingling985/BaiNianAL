import allure

import Page
from Base.base import Base


class PageAddress(Base):
    # 点击 地址管理
    def page_click_address_massage(self):
        self.base_click(Page.address_massage)
    # 点击 新增地址
    def page_click_new_address(self):
        self.base_click(Page.address_new_address)
    # 输入 收件人
    def page_input_receipt_name(self,receipt_name):
        self.base_input(Page.address_receipt_name,receipt_name)
    # 输入 手机号
    def page_input_add_phone(self,add_phone):
        self.base_input(Page.address_add_phone,add_phone)

    # 点击 所在区域
    def page_click_area(self,sheng,shi,qu):
        # 注：省、市、区
        self.base_click(Page.address_area)
        self.base_xpath_click(sheng)
        self.base_xpath_click(shi)
        self.base_xpath_click(qu)
    # 点击 所在区域--直辖市
    def page_click_area02(self,sheng,qu):
        # 注：省、市、区
        self.base_click(Page.address_area)           # 点击 所在地区
        self.base_xpath_click(sheng)
        self.base_click(Page.zhixiashikuang)   # 点击市 大框
        self.base_click(Page.zhixiashi)        # 选择 市
        self.base_xpath_click(qu)                    # 选择 区

    # 输入 详细地址
    def page_input_detail_address(self,address):
        self.base_input(Page.address_detail_addr,address)
    # 输入 邮编
    def page_input_post_code(self,postcode):
        self.base_input(Page.address_post_code,postcode)
    # 点击 设置默认地址
    def page_click_default(self):
        self.base_click(Page.address_default)
    # 点击 保存
    def page_click_button_save(self):
        self.base_click(Page.button_save)

    # 获取新增地址 收件人和电话【断言新增 方法一：】
    # def page_get_receipt_and_phone(self):
        # 获取新增地址(收件人+电话)所有元素
        # return self.base_get_text(Page.address_receipt_and_phone)

    # 获取一组元素的文本【断言新增 方法二：】
    def page_get_elements_text(self):     #【获取多个元素，先定位，在遍历文本】
        # 获取地址列表（收件人+电话）所有元素
        elements=self.base_find_elements(Page.address_receipt_and_phone)
        return [i.text for i in elements]


    # 点击编辑
    def page_click_cymtitlebar_right_btn(self):
        self.base_click(Page.address_ymtitlebar_right_btn)
    # 点击修改
    def page_click_xiugai(self,text='修改'):
        # 获取所有修改元素
        elements=self.base_xpaths(text)
        # 点击列表元素中第一个元素
        self.base_click_elements(elements)
    # 修改完 点击 保存
    def page_click_address_save_btn(self):
        self.base_xpath_click(Page.address_save_btn)


    # 点击删除
    def page_click_del(self,text='删除'):
        # 获取当前所有地址列表
        elements = self.base_find_elements(Page.address_receipt_and_phone)
        for i in range(len(elements)):
            # 点击 编辑
            self.page_click_cymtitlebar_right_btn()
            # 获取所有修改元素
            elements = self.base_xpaths(text)
            # 点击表元素中第一个元素删除
            self.base_click_elements(elements)
            # 点击确认删除
            self.base_click(Page.address_delete_ok)
    def page_is_del(self):
        try:
            self.base_find_elements(Page.address_receipt_and_phone,timeout=3)
            return False
        except:
            return True




















