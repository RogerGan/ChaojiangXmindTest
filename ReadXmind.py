# -*- coding:UTF-8 -*-

__author__ = 'gancj'

__data__ = '2015-05-23 10:47'

import xmind
from xmind.core import workbook,saver
from xmind.core.topic import TopicElement

w = xmind.load("test2.xmind") # load an existing file or create a new workbook if nothing is found
print w.getWorkbookElement()
print w.getSheets()
print w.getElementById(2)
print w.getPrimarySheet().getTitle()
print w.getPrimarySheet().getRootTopic().getTitle()

print w.getSheets()[1].getTitle()
print w.getSheets()[1].getRootTopic().getTitle()
#

print w.getSheets()[2].getTitle()
print w.getSheets()[2].getRootTopic().getID()
print w.getSheets()[2].getID()
print w.getSheets()[2].getChildNodesByTagName("test")

print w.getSheets()[2].getRootTopic().getSubTopics().__len__()

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

get_LSubTopics(w.getSheets()[2].getRootTopic())
print '------------------'
#终点节点的个数
print LSubTopics
print LSubTopics.__len__()

print getParentTopicByID_Dic
print getParentTopicByID_Dic.__len__()

print getTopicByID_Dic
print getTopicByID_Dic.__len__()

print '=============================='
#获取第一条用例的结尾部分
print LSubTopics[0].getTitle()
print LSubTopics[0].addMarker("yes")
#获取第一条用例的用例情况
print get_testcase_list(LSubTopics[0])


print '+++++++++++++++++++++++++++++'

xmind.save(w, "test3.xmind")