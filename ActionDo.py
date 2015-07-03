# -*- coding:UTF-8 -*-

__author__ = 'gancj'

__weibo__= 'http://weibo.com/ganchaojiang'

__data__ = '2015-05-28 10:11'

__mail__ = 'gancj@ucweb.com/393037282@qq.com'

from appium import webdriver
import anaysisXmind
import xmind
from time import sleep
import device_info
import string
import logging
import sys

reload(sys)
sys.setdefaultencoding('utf-8')


class ActionDo():
    '''
    action:动作
    element:动作的参数,可以有多个子参数
    '''
    def __init__(self, driver):
        self._driver = driver

    def Click(self, topic):

        action = topic.split(':')[0] #action :表示自动化测试的动作
        element = topic.split(':')[1:][0]   #element:动作的元素
        logging.info('action======{}  {} '.format(str(action), str(element)))
        try:
            self._driver.find_element_by_name(element).click()
            return 1
        except Exception, e:
            logging.warning('can\'t perform action {}  \terror info: {} '.format(element, e))
            return 2
    def ClickPoints(self, topic):
        self._driver.tap()

    def InputSth(self, topic):
        self._driver.execute_script("target.frontMostApp().keyboard().typeString('{0}')".format(topic))
        self._driver.execute_script("target.frontMostApp().keyboard().typeString('\\n')")

    def Shake(self, topic):
        self._driver.shake()

    def Lock(self, topic):
        self._driver.lock()

    def ClickWeb(self, topic):
        action = topic.split(':')[0] #action :表示自动化测试的动作
        element = topic.split(':')[1:][0]   #element:动作的元素
        logging.info('action======{} , {}'.format(action, element))
        self._driver.find_element_by_xpath('//*[@name="' + element + '"]').click()

    def Wait(self, topic):
        action = topic.split(':')[0] #action :表示自动化测试的动作
        element = topic.split(':')[1:][0]   #element:动作的元素
        content = topic.split(':')[1:][1]   #content:动作元素的内容
        logging.info('action====== {} {} {}'.format(action, element, content))
        sleep(element * 1000)

    def Swipe(self, topic):
        '''
            Sample: Swpie:Left
        '''

        action = topic.split(':')[0] #action :表示自动化测试的动作
        element = topic.split(':')[1:][0]   #element:动作的元素
        logging.info('action====== {}  {}'.format(action, element))
        pointleft = device_info.device_screen[2]*1 / 5
        pointright = device_info.device_screen[2]*4 / 5
        pointup = device_info.device_screen[3]*1 / 4
        pointdown = device_info.device_screen[3]*3 / 4
        if element == "Left":
            self._driver.swipe(pointright, device_info.device_screen[3]/2, pointleft, device_info.device_screen[3]/2)
        elif element == "Right":
            self._driver.swipe(pointleft, device_info.device_screen[3]/2, pointright, device_info.device_screen[3]/2)
        elif element == "Up":
            self._driver.swipe(device_info.device_screen[2]/2, pointdown, device_info.device_screen[2]/2, pointup)
        elif element == "Down":
            self._driver.swipe(device_info.device_screen[2]/2, pointup, device_info.device_screen[2]/2, pointdown)

    def Input(self, topic):
        action = topic.split(':')[0] #action :表示自动化测试的动作
        element = topic.split(':')[1:][0]   #element:动作的元素
        content = topic.split(':')[1:][1]   #content:动作元素的内容
        logging.info('action====== {} {} {}'.format(action, element, content))
        self._driver.find_element_by_name(element).set_value(content)

    def ScreenShot(self, topic):
        action = topic.split(':')[0] #action :表示自动化测试的动作
        element = topic.split(':')[1:][0]   #element:动作的元素
        logging.info('action====== {} {}'.format(action, element))
        self._driver.get_screenshot_as_file(element)

    def Check(self, topic):
        action = topic.split(':')[0] #action :表示自动化测试的动作
        element = topic.split(':')[1:][0]   #element:动作的元素
        logging.info('action====== {}  {}'.format(action, element))
        try:
            self._driver.find_element_by_name(element)
            return 1
        except Exception, e:
            logging.warning('Can\'t find'.format(element))
            return 0

    def Module(self, topic):
        return 1