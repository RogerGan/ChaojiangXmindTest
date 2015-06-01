# -*- coding:UTF-8 -*-

__author__ = 'gancj'

__data__ = '2015-05-23 12:06'

from appium import webdriver
import anaysisXmind
import xmind
from time import sleep
import device_info
import string
import ActionDo

res = xmind.load("test2.xmind")

driver = webdriver.Remote(
    command_executor='http://127.0.0.1:4723/wd/hub',
    desired_capabilities={
            "bundleId" : "ninegame.ucweb.iphone",
            "udid" : "9eef767be4750283f20069295e839abfb0321444",
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
    #用例个数
    num = anaysisXmind.get_LSubTopics(res.getSheets()[2].getRootTopic()).__len__()
    print num
    ad = ActionDo.ActionDo(driver)

    for i in xrange(num):
        actions = anaysisXmind.get_testcase("test2.xmind", 2, i)
        print 'actions', actions
        for action in actions:
            doaction = action.split(':')[0]
            result = getattr(ad, doaction, 'Error! para Error')(action)

            if result != 1 and result != 0: #不是结果检查的问题
                print 'Action do Error'
                break

        if result == 1:
            print 'add Check Pass Marker'
            result_dict[i] = 1
        elif result == 0:
            print 'add Check Fail Marker'
            result_dict[i] = 0
        elif result == 2:
            print 'add Action Fail Marker'
            result_dict[i] = 2

    return result_dict

if __name__ == "__main__":
    print testAction()
    tearDown()
    print ''