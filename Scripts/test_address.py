import os,sys
sys.path.append(os.getcwd())
import allure
import pytest
from Base.read_yaml import ReadYaml
from Page.page_in import PageIn
from Base.get_driver import get_driver


def get_data03():
    datas=ReadYaml('address.yaml').read_yaml()
    data=datas.get('add_address').values()
    arrs=[]
    for data in datas.get('add_address').values():
        arrs.append((data.get("receipt_name"), data.get("add_phone"), data.get("sheng"), data.get("shi"), data.get("qu"), data.get("address"), data.get("postcode")))
    return arrs

def get_data04():
    datas=ReadYaml('address.yaml').read_yaml()
    data=datas.get('updata_address').values()
    arrs=[]
    for data in datas.get('updata_address').values():
        arrs.append((data.get("receipt_name"), data.get("add_phone"), data.get("sheng"), data.get("shi"), data.get("qu"), data.get("address"), data.get("postcode"), data.get("toast_expect")))
    return arrs



class TestAddress():
    def setup_class(self):
        # 登录成功
        self.page=PageIn(get_driver())
        self.page.page_get_login().page_login('18610453007','123456')
        # 点击设置
        self.page.page_get_login().page_click_setting()
        # 实例化 地址管理页面类 PageAddress
        self.address = self.page.page_get_address()
        # 点击 地址管理
        self.address.page_click_address_massage()
    def teardown_class(self):
        # 退出driver驱动
        self.page.driver.quit()

    '''【地址增加】'''
    @pytest.mark.run(order=1)
    @pytest.mark.parametrize("receipt_name,add_phone,sheng,shi,qu,address,postcode", get_data03())
    def test_add_address(self,receipt_name,add_phone,sheng,shi,qu,address,postcode):
        addr=self.address
        # 点击 新增地址
        addr.page_click_new_address()
        # 输入 收件人
        addr.page_input_receipt_name(receipt_name)
        # 输入 手机号
        addr.page_input_add_phone(add_phone)
        # 选择 所在区域
        addr.page_click_area(sheng,shi,qu)

        # 选择 所在区域 - -直辖市
        # addr.page_click_area02("北京","海淀区")

        # 输入 详细地址
        addr.page_input_detail_address(address)
        # 输入 邮编
        addr.page_input_post_code(postcode)
        # 点击 设置默认地址
        addr.page_click_default()
        # 点击 保存
        addr.page_click_button_save()

        try:
            # print('新增地址联系人和电话为：',addr.page_get_receipt_and_phone())
            # (断言新增 方法一：）
            # assert receipt_name in addr.page_get_receipt_and_phone()
            """方法二：通过后去地址列表所有的收件和电话"""
            name_phont=receipt_name+"  "+add_phone
            assert name_phont in addr.page_get_elements_text()
        except:
            # 截图
            self.login.base_getImage()
            with open("./Image/faild.png", "rb") as f:
                allure.attach("断言失败：", f.read(), allure.attach_type.PNG)
            raise


    '''【地址修改】'''
    @pytest.mark.run(order=2)
    @pytest.mark.parametrize("receipt_name,add_phone,sheng,shi,qu,address,postcode,toast_expect", get_data04())
    def test_xiugai_address(self,receipt_name,add_phone,sheng,shi,qu,address,postcode,toast_expect):
        addr=self.address
        # 点击编辑
        addr.page_click_cymtitlebar_right_btn()
        # 点击修改
        addr.page_click_xiugai()
        # 输入 收件人
        addr.page_input_receipt_name(receipt_name)
        # 输入 手机号
        addr.page_input_add_phone(add_phone)
        # 选择 所在区域
        addr.page_click_area(sheng,shi,qu)
        # 输入 详细地址
        addr.page_input_detail_address(address)
        # 输入 邮编
        addr.page_input_post_code(postcode)
        # 点击 保存
        addr.page_click_address_save_btn()
        try:
            """方法一：更新后的用户名+电话，是否在地址列表中"""
            # name_phont=receipt_name+"  "+add_phone
            # assert name_phont in addr.page_get_elements_text()
            """第二种断言更新是否成功：根据toast消息  保存成功"""
            assert toast_expect in self.address.base_get_toast(toast_expect)
        except:
            # 截图
            self.login.base_getImage()
            with open("./Image/faild.png", "rb") as f:
                allure.attach("断言失败：", f.read(), allure.attach_type.PNG)
            raise



    '''【地址删除】'''
    @pytest.mark.run(order=3)
    def test_del_address(self):
        addr = self.address
        # 删除
        addr.page_click_del()
        try:
            assert addr.page_is_del()
        except:
            # 截图
            self.login.base_getImage()
            with open("./Image/faild.png", "rb") as f:
                allure.attach("断言失败：", f.read(), allure.attach_type.PNG)
            raise

















