import os
import time
import traceback
from telnetlib import EC
from time import sleep
import win32api
import win32con
from selenium.webdriver import ActionChains
from selenium.webdriver.common import by
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait


def currentDate():
    """生成当前日期字符串"""
    date = time.localtime()
    return '-'.join([str(date.tm_year), str(date.tm_mon), str(date.tm_mday)])


def currentTime():
    """生成当前时间字符串"""
    date = time.localtime()
    return '-'.join([str(date.tm_hour), str(date.tm_min), str(date.tm_sec)])


def createDir():
    """创建当前日期和当前时间目录"""
    path = os.path.dirname(os.path.abspath(__file__))
    dateDir = os.path.join(path, currentDate())
    # 如果当前日期目录不存的话就创建
    if not os.path.exists(dateDir):
        os.mkdir(dateDir)
    timeDir = os.path.join(dateDir, currentTime())
    # 如果当前时间目录不存的话就创建
    if not os.path.exists(timeDir):
        os.mkdir(timeDir)
    return timeDir


def takeScreenshot(driver, savePath, pictureName):
    picturePath = os.path.join(savePath, pictureName + '.png')
    try:
        driver.get_screenshot_as_file(picturePath)
    except Exception as e:
        print(traceback.print_exc(e))


class Common(object):

    def __init__(self, driver):
        self.driver = driver

    # 模拟键盘按键类
    VK_CODE = {
        'enter': 0x0D,
        'ctrl': 0x11,
        'c': 0x43,
        'v': 0x56,
        'i': 0x49,
        'down': 0x28,
        'up': 0x26,
        'left': 0x25,
        'right': 0x27,
        'shift': 0x10
    }

    @staticmethod
    def keyDown(keyName):
        # 按下按键
        win32api.keybd_event(Common.VK_CODE[keyName], 0, 0, 0)

    @staticmethod
    def keyUp(keyName):
        # 释放按键
        win32api.keybd_event(Common.VK_CODE[keyName], 0, win32con.KEYEVENTF_KEYUP, 0)

    @staticmethod
    def oneKey(key):  # 对前两个方法的调用
        # 模拟单个按键
        Common.keyDown(key)
        Common.keyUp(key)

    @staticmethod
    def onekey_down(key):
        Common.keyDown(key)

    @staticmethod
    def onekey_up(key):
        Common.keyUp(key)

    @staticmethod
    def twoKeys(key1, key2):  # 对前面函数的调用
        # 模拟两个组合键
        Common.keyDown(key1)
        Common.keyDown(key2)
        Common.keyUp(key2)
        Common.keyUp(key1)

    def location(self, location):
        """
        元素定位
        :param location: 元素定位路径
        :return:
        """
        el = self.driver.find_element(*location)
        return el

    def element_send_keys(self, location, text):
        """
        输入
        :param location: 元素定位路径
        :param text: 输入的文本内容
        :return:
        """
        self.location(location).send_keys(text)
        sleep(0.5)

    def input_clear(self, location):
        """
        清空文本框
        :param location: 元素的定位路径
        :return:
        """
        self.location(location).clear()

    def select(self, location, text):
        """
        下拉框选择
        :param location:
        :param text:
        :return:
        """
        el = self.location(location)
        Select(el).select_by_value(text)

    def switch_handles(self):
        """
        切换句柄
        :return:
        """
        handles = self.driver.switch_to.window()
        self.driver.switch_to.window(handles[1])

    def switch_iframe(self, location):
        """
        切换iframe
        :param location:
        :return:
        """
        el = self.location(location)
        self.driver.switch_to.frame(el)

    def out_iframe(self):
        """
        从当前切换到主文档
        :return:
        """
        self.driver.switch_to.default_content()

    def back_up_iframe(self):
        """
        嵌套iframe切换到上一级iframe
        :return:
        """
        self.driver.switch_to.parent_frame()  # 如果当前已是主文档，则无效果

    def key_enter(self, location):
        """
        按下ENTER
        :param location:
        :return:
        """
        el = self.location(location)
        el.send_keys(Keys.ENTER)

    def ctrl_c(self, location):
        """
        ctrl+c
        :param location:
        :return:
        """
        self.location(location).send_keys(Keys.CONTROL + 'c')

    def alt_c(self, location):
        """
        alt+c
        :param location:
        :return:
        """
        self.location(location).send_keys(Keys.ALT + 'c')

    def element_click(self, location):
        """
        鼠标左键单击
        :param location:
        :return:
        """
        self.location(location).click()
        sleep(0.5)

    def double_click(self, location):
        """
        双击事件
        :param location:
        :return:
        """
        el = self.location(location)
        ActionChains(self.driver).double_click(el).perform()

    def mouse_hover(self, location):
        """
        鼠标悬停
        :param location:
        :return:
        """
        e1 = self.location(location)
        ActionChains(self.driver).move_to_element(e1).perform()

    def web_driver_wait(self, location, _time, text):
        """
        显示等待
        :param location: 查找的元素的路径
        :param _time: 等待时间
        :param text: 异常返回的指定信息
        :return:
        """
        WebDriverWait(self.driver, _time, 0.5).until(lambda el: self.location(location), message=text)

    @staticmethod
    def upload_file(exe, browser, filename):
        """
        使用autoIt上传文件
        :param exe: 上传文件的exe程序所在目录
        :param browser: 浏览器类型： firefox chrome ie
        :param filename: 待上传文件路径
        :return: none
        """
        cmd = exe + ' ' + browser + ' ' + filename
        os.system(cmd)

    def screenshot(self):
        self.driver.get_screenshot_as_file()

    def js_scroll_top(self):
        """
        滚动到顶部
        :return:
        """
        js = "document.documentElement.scrollTop=0"
        self.driver.execute_script(js)

    def js_scroll_middle(self):
        """
        滚动到页面中部
        :return:
        """
        js = "window.scrollBy(0, 0-document.body.scrollHeight *1/2)"
        self.driver.execute_script(js)

    def js_scroll_bottom(self):
        """
        滚动到底部
        :return:
        """
        js = "document.documentElement.scrollTop=10000"
        self.driver.execute_script(js)

    def back(self):
        """
        返回之前的网页
        :return:
        """
        self.driver.back()

    def forward(self):
        """
        前往下一个网页
        :return:
        """
        self.driver.forward()

    def close(self):
        """
        关闭当前网页
        :return:
        """
        self.driver.close()

    def quit(self):
        """
        关闭所有网页，退出浏览器
        :return:
        """
        self.driver.quit()

    def kill_chrome(self):
        """
        杀死Chrome浏览器进程
        :return:
        """
        code = os.system("taskkill /F /im chrome.exe")
        if code == 0:
            print("kill chrome successfully")
        else:
            print("kill chrome failed")
