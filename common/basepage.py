#:@ TIME 2021/12/24   17:54
#:@FILE  basepage.py
#:@EMAIL  1557225637@QQ.COM

from my_py.pathFunc import error_picture_dir
import time
import os
from common.log import log
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Base_page:
    '''
    def waite_ele_visible：封装的等待元素可见方法 #打印-计时-try-等待-expect-打印-截图-r-else打印等待时长

    def get_element(self,loc,page_action): 封装的 find 元素方法 ，打印-调用封装好的等待-try-查找元素-expect  打印失败-截图-raise-else-return 元素


    '''

    def __init__(self, drever: WebDriver):
        self.driver = drever

    # 封装等待方法
    # 打印-计时-try-等待-expect-打印-截图-else打印等待时长
    def __waite_ele_visible(self, loc, page_action, time_out):
        # log输出 什么元素
        # log.info('等待元素：({}) 可见,action({})'.format(loc, page_action))
        # 等待开始时间
        start = time.time()
        # 捕捉异常
        try:
            WebDriverWait(self.driver, time_out).until(EC.visibility_of_element_located(loc))
            # WebDriverWait(self.driver,time_out).until(EC.presence_of_all_elements_located(loc))

        except:
            # 输出等待失败
            log.exception("等待元素可见失败,loc:({})".format(loc))
            # 调用失败截图方法
            self.get_page_img(page_action)
            raise
        else:
            pass
            # end = time.time()
            # log.info('等待元素成功，等待时间为:{}'.format(start - end))

    # 打印-调用封装好的等待-try-查找元素-expect  打印失败-截图-raise-else-return 元素
    def get_element(self, loc, page_action, index=None, time_out=20):
        self.__waite_ele_visible(loc, page_action, time_out)
        # log.info('获取元素对象 loc({}),action({})'.format(loc, page_action))
        if index:
            try:
                loc_obj = self.driver.find_elements(*loc)[index]
            except:
                log.info("获取元素对象失败,loc({})".format(loc))
                self.get_page_img(page_action)
                raise
            else:
                return loc_obj
        else:
            try:
                loc_obj = self.driver.find_element(*loc)
            except:
                log.exception("查找:{} 元素失败".format(loc))
                # 调用失败截图方法
                self.get_page_img(page_action)
                raise
            else:
                return loc_obj

    # 打印-调用封装的geielement-try-调用查找元素方法-expect-dayin-截图-raise
    def click_element(self, loc, page_action, index=None, time_out=20):
        loc_obj = self.get_element(loc, page_action, index, time_out)
        try:
            # log.info('准备 click元素：{} ,action({})'.format(loc, page_action))
            loc_obj.click()
        except:
            log.exception("点击元素失败,action:({}),lco:({})".format(page_action, loc))
            # 调用失败截图方法
            self.get_page_img(page_action)
            raise

    # 打印-调用封装的getelement-try-输入参数-expect-输入文本失败-截图-raise-else-打印
    def input_value(self, loc, page_action, value, index=None, time_out=20):
        loc_obj = self.get_element(loc, page_action, index, time_out)
        try:
            # log.info('input元素：{}'.format(page_action, loc))
            loc_obj.clear()
            loc_obj.send_keys(value)
        except:
            log.exception('输入文本失败,loc({})'.format(loc))
            self.get_page_img(page_action)
            raise

        else:
            # log.info('value 输入成功,value为：{}'.format(value))
            pass

    # 打印-调用封装的getelement-try-获取文本-expect-获取文本失败-截图-raise-else-return-tetx
    def get_text(self, loc, page_action, index=None, time_out=5):
        # 获取元素对象
        loc_obj = self.get_element(loc, page_action, index, time_out)
        try:
            # log.info('在 {} 行为，获取元素文本:{}'.format(page_action, loc))
            # 获取文本
            text_obj = loc_obj.text
        except:
            log.exception('获取文本失败, loc:({})'.format(loc))
            self.get_page_img(page_action)
            raise
        else:
            # log.info('获取文本元素成功，元素为：{}'.format(text_obj))
            return text_obj

    # 页面截图方法
    def get_page_img(self, page_action):
        # 命名规范 XX页面XX操作XX截图时间

        # 当前时间
        current_time = time.strftime('%Y-%m-%d-%H-%M-%S', time.localtime())
        # 文件名称
        file_path = os.path.join(error_picture_dir, '{}_{}.png'.format(page_action, current_time))
        # 调用截图方法 传入文件路径
        self.driver.save_screenshot(file_path)

    def swich_to_window(self, name='new'):

        time.sleep(1)
        if name == 'new':
            log.info('获取当前 浏览器所有窗口句柄')
            win_s = self.driver.window_handles
            try:
                log.info('准备切换到最新窗口')
                driver.switch_to.window((win_s[-1]))
            except:
                log.exception('切换到新窗口失败')
            else:
                log.info('成功切换到新窗口')


if __name__ == '__main__':
    driver = webdriver.Chrome()
    new_basepage = Base_page(driver)
    driver.maximize_window()
    driver.get('https://www.baidu.com/')

    loc = (By.ID, 'kw')
    new_basepage.input_value(loc, '百度输入框输入文本', '柠檬班')
