# -*- coding:UTF-8 -*-

__author__ = 'gancj'

__data__ = '2015-07-03 11:52'

__mail__ = 'gancj@ucweb.com/393037282@qq.com'

import os
import ConfigParser

def getDevID():
    '''获取真机设备udid.
    Args:无
    Returns:无
    '''
    all_devid = os.popen('system_profiler SPUSBDataType | grep "Serial Number:.*" | sed s#".*Serial Number: "##').readlines()
    devid = ''
    i = 0
    while (i < len(all_devid)):
        if len(all_devid[i]) >= 40:
            devid = all_devid[i].replace("\n", '')
            break
        i += 1
    return devid

def anaysisIniFile(filepath, section, key):
    cf = ConfigParser.ConfigParser()
    cf.read(filepath)
    return cf.get(section, key)