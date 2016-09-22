# -*- coding: utf-8 -*-
#coding:utf-8
#-------------------------------------------------------------------------------
# Name:        文件写入类模块
# Purpose:
#
# Author:      zhangxin
#
# Created:     12/09/2016
# Copyright:   (c) Administrator 2016
# Licence:     <your licence>
#-------------------------------------------------------------------------------

class Writer:
    def __init__(self, path):
        self.fo = open(unicode(path), "wb")

    def wr(self, content):
        self.fo.write(content)

    def flush(self):
        self.fo.flush()

    def close(self):
        self.fo.close()
