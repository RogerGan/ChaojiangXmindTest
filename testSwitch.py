# -*- coding:UTF-8 -*-

__author__ = 'gancj'

__data__ = '2015-05-23 10:20'

import unittest
from random import randint
from appium import webdriver
from time import sleep

class SimpleIOSTests(unittest.TestCase):

    def setUp(self):
        # set up appium
        self.driver = webdriver.Remote(
            command_executor='http://127.0.0.1:4723/wd/hub',
            desired_capabilities={
                    "bundleId" : "ninegame.ucweb.iphone",
                    "udid" : "e25a0119877c106940688a647ff3d070678c856d",
                    "deviceName" : "iphone",
                    "platformName" : "iOS",
                    "platformVersion" : "7.1",
                    "autoAcceptAlerts": "true"
            })

    def tearDown(self):
        self.driver.quit()

    def test_scroll(self):
        print ''
        self.driver.tap()
        self.driver.find_element_by_name(u'发现').click()
        sleep(3)


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(SimpleIOSTests)
    unittest.TextTestRunner(verbosity=2).run(suite)