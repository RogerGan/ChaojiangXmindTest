# -*- coding:UTF-8 -*-

__author__ = 'gancj'

__data__ = '2015-05-23 11:37'

import xmind
import logging

LSubTopics = []  #终点节点
getParentTopicByID_Dic = {}
getTopicByID_Dic = {}

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
            getParentTopicByID_Dic[subtopic.getID()] = topic
            getTopicByID_Dic[subtopic.getID()] = subtopic
    return LSubTopics

def testcase_list_init(topic, testcase_list):

    if topic.getType() == "root":
        testcase_list.append(topic)
        return
    else:
        testcase_list.append(topic)
        testcase_list_init(getParentTopicByID_Dic[topic.getID()] ,testcase_list)

def get_testcase_list(topic):
    testcase_list = []
    testcase_list_init(topic ,testcase_list)

    return testcase_list

def get_testcase(xmindfile, sheet, index):
    w = xmind.load(xmindfile) # load an existing file or create a new workbook if nothing is found
    testcase = []
    get_LSubTopics(w.getSheets()[sheet].getRootTopic())
    length = get_testcase_list(LSubTopics[index]).__len__()
    for i in xrange(length):
        testcase.append(get_testcase_list(LSubTopics[index])[length-i-1].getTitle())
    return testcase

if __name__ == "__main__":
    get_LSubTopics(xmind.load("test2.xmind").getSheets()[2].getRootTopic())
    logging.info(get_testcase("test2.xmind", 2, 0))
    for i in xrange(5):
        actions = get_testcase("test2.xmind", 2, i)
        logging.info('actions  {}'.format(actions))