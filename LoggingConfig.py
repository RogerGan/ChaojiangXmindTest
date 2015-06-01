# -*- coding:UTF-8 -*-

__author__ = 'gancj'

__data__ = '2015-05-30 11:28'

__mail__ = 'gancj@ucweb.com/393037282@qq.com'

import logging

logging.basicConfig(level=logging.NOTSET,
                format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                datefmt='%a, %d %b %Y %H:%M:%S',
                filename='XmindTest.log',
                filemode='a')

#################################################################################################
#定义一个StreamHandler，将NOTSET级别或更高的日志信息打印到标准错误，并将其添加到当前的日志处理对象#
#日志级别大小关系为：CRITICAL > ERROR > WARNING > INFO > DEBUG > NOTSET，分别的数值大小是,50,40,...0,当然也可以自己定义日志级别。
console = logging.StreamHandler()
console.setLevel(logging.NOTSET)
formatter = logging.Formatter('%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s')
console.setFormatter(formatter)
logging.getLogger('').addHandler(console)
#################################################################################################
