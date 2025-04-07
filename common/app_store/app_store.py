from selenium import webdriver
import time
from user_data import *
from common.basepage import Base_page
from selenium.webdriver.common.by import By

first_click_button = By.XPATH, '//span[text()="英文（美国）"]'
driver = webdriver.Chrome()
url = 'https://appstoreconnect.apple.com/apps/1130649335/appstore/ios/version/inflight'
new_cookie = {"name": "myacinfo",
              "value": "DAWTKNV323952cf8084a204"
                       ""
                       ""
                       "fb20ab2508441a07d02d37c5d6ab30827422818a8d53be98d9c7884f6a2f09a205aea68d5a7b650bd5d431154700846c3b0058257d062bfa01b62f3e886269c1f275e38b879211a890e4d1d3e8e55c52db32043e5b14e75a1952bd66fe5d34b89be680d39692e4a1d5f5c2a76496b3c5088c9d000505fd484079be3cfa58f87d0655c80399415bc5f9c5851e943635fbc037741820d7765751e8dbc7cc1c9e015a8337e83f8e93e709c8ef1bc60d3e02a875b9e8bfdff27d9bb9415b2408a9bf90d1e73c02ddb4437558c870e76f564f7f5036f3bd269f29e6f38c7e91b7c37b4c577b824cbf88da819a1e2534643c4e728ce8476513969971d8f523cc81ba732df1c0fce2e478675fe544f40c297ba51f2cb92704c83bef39a7813f495ed2c210e799d96ca0a46df82ddca582b251eb60403acbf52df5e5f7837618312f26c24c29018917ef27ff04336e75d4b4ec5e7dfc101d125e2bed510012dc9dac88dde600a26484513cf3d162b01b2e5c387d802a711f299d7103615cbaec7855cffe54e718ccfa06ca207977b44c0c4f3d4f86f51982619bdcfe1a98553c4837ef5326baf268c38369cbdf19499fcf2123508793a7e04cb8b0c31f13b0293d2a9fc86cc1fae30f9ef9fe623d7604bf620b3502198735d8493cfbe639da205c10e163c96fcc10e9bdae9bf3e3b70b01e945b99bb329cf969758dbf21a378843f416cc39860ab6140ddd3960ef8585a47V3"}


class AppStore(Base_page):
    driver.get(url)
    driver.maximize_window()
    driver.add_cookie(new_cookie)
    time.sleep(1)
    driver.get(url)

    def switch_country(self, country_loc):
        self.click_element(country_button_loc, '点击切换国家', index=1)
        self.click_element(country_loc, '点击切换到国家')

    def run(self):
        pass
        # self.click_element()
        time.sleep(10)
        for i in country_list:
            self.switch_country(i['loc'])
            loc = i['v1']
            self.input_value(promotion_input_box_loc, f'输入推广文本，loc:({loc =})', i['v1'])
            self.input_value(new_describe_loc, '输入本次新增内容', i['v2'])
            self.click_element(save_button_loc, '点击存储按钮')
            time.sleep(5)


app = AppStore(driver)
app.run()
