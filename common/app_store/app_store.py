from selenium import webdriver
import time
from user_data import *
from common.basepage import Base_page

driver = webdriver.Chrome()
url = 'https://appstoreconnect.apple.com/apps/1130649335/appstore/ios/version/inflight'
new_cookie = {"name": "myacinfo", "value": "DAWTKNV323952cf8084a204fb20ab2508441a07d02d31e28ed5440190d32f16773d0cf6a2"
                                           "d246e6f75ae35b853633dad7d35ac46e9b380cf3b490af3c0ca86d7991c20b905583f1237"
                                           "726076cbf1c6f07ac8658422c39d9161c31fd3249f9c6aec878ff6d5254699c26a78cbade"
                                           "a6b55b8047280b16f4eebf3aab66938eabe65446b845a2fd0a71a60778b6da01e00e031a9"
                                           "67958e8a675c92e9bcc0b0983b83f0bfd12a7cec39a3075f16207c53c8612f48635cea687"
                                           "62e5ed98afc8c80fb03c58ef3613068fa1251be55132a8515398fc7152ba1574c46c50b38"
                                           "b3e7c331c0661b4a916b8141893a366ef7f510107ffaf5eaadeaea2ef6ef1f8927999b948"
                                           "b20ef3dae88d7e6f22ad81095fc58161d1585e12b499ac2f480bf793c463a709125459add"
                                           "df144c0e5ac2adeeb0bd3502302806e5fd5626ee70d5d3ed43a8e1b46a7aab607df121659"
                                           "d73c4338970ac066902d48b6dde164cc6f25d69c6aa8b7ef4a3ff1540ee8b83b9f7b5fc5e"
                                           "b8afdf58666ff573b070c861307c5a670d03daa97d0ef6870abab43626491ca47770c3e38"
                                           "deea3132a6edcc95fd260ce246e63bf9edb3d2c47329512731db59dc976accc9188444269"
                                           "ec2df0a9f8117975017451d4b18f1468cabb6b6a13ddd9f99eb1850d3d517ef995c94ed02"
                                           "e650065307b0ced7ce89ba143313ec072a9f276da8e908389d02515ab6643cd3aac4bf814"
                                           "251a919b66fe98585a47V3"}


class AppStore(Base_page):
    driver.get(url)
    driver.maximize_window()
    driver.add_cookie(new_cookie)
    driver.get(url)

    def switch_country(self, country_loc):
        self.click_element(country_loc, '点击切换国家', index=0)
        self.click_element(country_loc, '点击切换到国家')

    def run(self):
        for i in country_list:
            self.switch_country(i['loc'])
            self.input_value(promotion_input_box_loc, '输入推广文本', i['v1'])
            self.input_value(new_describe_loc, '输入本次新增内容', i['v2'])
            time.sleep(1)
            self.click_element(save_button_loc, '点击存储按钮')


app = AppStore(driver)
app.run()
