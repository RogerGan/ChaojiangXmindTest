# -*- coding:UTF-8 -*-

__author__ = 'gancj'

__data__ = '2015-05-23 16:35'

import Action
import xmind
import BaseTools.util

from xmind.core.markerref import MarkerId
import logging
import loggingconfig

loggingconfig.open_logging()


inputxmindfile = BaseTools.util.anaysisIniFile('config.ini', 'xmind_args', 'inputxmindfile')
logging.warning(inputxmindfile)
res = xmind.load(inputxmindfile)


LSubTopics = []  #终点节点

'''
    获取多少条用例
    遍历到每条路径的最后一个节点为准，代表个数
'''
def get_LSubTopics(topic):
    #初始化主题关系链
    if topic.getSubTopics() == None:
        LSubTopics.append(topic)

    else:
        for subtopic in topic.getSubTopics():
            get_LSubTopics(subtopic)


if __name__ == "__main__":
    # try:
    result_dict = Action.testAction()
    Action.tearDown()
    # except KeyboardInterrupt:
    #     Action.tearDown()

    get_LSubTopics(res.getSheets()[0].getRootTopic())

    for key in result_dict:
        if result_dict[key] == 1:
            LSubTopics[key].getTitle()
            LSubTopics[key].addMarker(MarkerId.smileyLaugh) #用例通过，开心
            logging.info('{0} is pass，Laugh'.format(key))
        elif result_dict[key] == 0:
            logging.info('{0} is fail, Cry'.format(key))
            LSubTopics[key].addMarker(MarkerId.smileyCry)   #用例失败，难过
        elif result_dict[key] == 2:
            logging.info('{0} actions fail'.format(key))
            LSubTopics[key].addMarker(MarkerId.symbolWrong) #测试用例有问题，一把叉

    xmind.save(res, "test3.xmind")