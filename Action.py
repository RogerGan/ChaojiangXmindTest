# -*- coding:UTF-8 -*-

__author__ = 'gancj'

__weibo__= 'http://weibo.com/ganchaojiang'

__data__ = '2015-05-23 12:06'

from appium import webdriver
import anaysisXmind
import xmind
import logging

import device_info
import ActionDo
import BaseTools.util

inputxmindfile = BaseTools.util.anaysisIniFile('config.ini', 'xmind_args', 'inputxmindfile')
logging.warning(inputxmindfile)
res = xmind.load(inputxmindfile)

driver = webdriver.Remote(
    command_executor='http://127.0.0.1:4723/wd/hub',
    desired_capabilities={
            "bundleId" : "cn.ninegame.gamemanager",
            "udid" : "{}".format(device_info.device_udid),
            "deviceName" : "gancj",
            "platformName" : "iOS",
            "platformVersion" : "8.3",
            "autoAcceptAlerts": "true"
    })

def tearDown():
    driver.quit()

#topic = u'Click:\u6d88\u606f'

def testAction():
    result_dict = {}
    #第一张表的用例个数
    num = anaysisXmind.get_LSubTopics(res.getSheets()[0].getRootTopic()).__len__()
    logging.info('测试用例个数:{}'.format(num))
    ad = ActionDo.ActionDo(driver)

    for i in xrange(num):
        actions = anaysisXmind.get_testcase("test2.xmind", 0, i)
        logging.info('actions'.format(actions))
        for action in actions:
            doaction = action.split(':')[0]
            result = getattr(ad, doaction, 'Error! para Error')(action)

            if result != 1 and result != 0: #不是结果检查的问题
                logging.warning('Action do Error')
                break

        if result == 1:
            logging.info('add Check Pass Marker')
            result_dict[i] = 1
        elif result == 0:
            logging.info('add Check Fail Marker')
            result_dict[i] = 0
        elif result == 2:
            logging.info('add Action Fail Marker')
            result_dict[i] = 2

    return result_dict

if __name__ == "__main__":
    logging.info(testAction())
    tearDown()