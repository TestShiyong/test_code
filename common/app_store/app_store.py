from selenium import webdriver
import time
from user_data import *
from common.basepage import Base_page

driver = webdriver.Chrome()
url = 'https://appstoreconnect.apple.com/apps/1130649335/appstore/ios/version/inflight'
new_cookie = {"name": "myacinfo",
              "value": "DAWTKNV323952cf8084a204fb20ab2508441a07d02d361627bfe78cb9a07b876889ad6bcb53a8532dbc8b3e876a16db3bfcabbbd4a1faa964902e0ee4e8db5a3cec8bf97d3ad728f740ab538ba4d6bd9f34abf871824275643e0b2694a9d66fd1f7b5f739cc43ad94b3ec65e8d2d5dee09fc91821880d4788f4b7ecb9b99cc42e8dc9209d8ff69f448f96f7cd87cb1a1813c5ff89283d17cca81edb8500c3480e5d515ef80b815dbd52dad54ea4b421deaabe6139b8f622377faf447ec261b30b744c084852a7df3fa558a35eb5257651cb6963bfbe6bd5fdca3340b811903f36b161910413e93e7638382c1443839204cc0e572bb53946e05844fd774a8eb3e3dc3d3055cdc0515fa746fa0839e57028a7b970666fb5961f782032c274c76d2ab9245d3c1ba76f2ac96e65fe6e2d102cf7447322fa96f053ec7046d599733bfc861fa568b85aed0cc91bd75b0cdf744cd4e118e4eed7e0649cc30150c43a7e4ea638cf9d75dd5170b4c1dfe868792eae211669d7da82d783d6b5531f74644b20d49b4b0af0c8a6170eea9bac8d966df0f4e3ffb52c49ae3615d5f29355646048e9344cc8ff9cd52faf9e43b79a7a435d6b133347b216040125d6d7c9c11886c7e940cb301affdd5119c10263508e77f286c7f6e363ec728ced0491bbb4ec17b86323c5643aeafd48e38c013391b7cf7a82adab90dae2158e76785f369578c319fac25ee577a7d8521172d170aa913faeb8d9d7f559a585a47V3"}


class AppStore(Base_page):
    driver.get(url)
    driver.maximize_window()
    driver.add_cookie(new_cookie)
    driver.get(url)

    def switch_country(self, country_loc):
        self.click_element(country_button_loc, '点击切换国家', index=0)
        self.click_element(country_loc, '点击切换到国家')

    def run(self):
        for i in country_list:
            self.switch_country(i['loc'])
            loc = i['v1']
            self.input_value(promotion_input_box_loc, f'输入推广文本，loc:({loc =})', i['v1'])
            self.input_value(new_describe_loc, '输入本次新增内容', i['v2'])
            self.click_element(save_button_loc, '点击存储按钮')
            time.sleep(5)


app = AppStore(driver)
app.run()
