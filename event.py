# coding:utf-8
# -*- coding: UTF-8 -*- 。
# -------------------------------------------------------------------------------
# Name:        事件实体类模块
# Purpose:
#
# Author:      zhangxin
#
# Created:     12/09/2016
# Copyright:   (c) Administrator 2016
# Licence:     <your licence>
# -------------------------------------------------------------------------------

# 事件实体类

class Event:
    def __init__(self, id, name, news, start, end, stock, weight, quanpin, jianpin, valid, titles):
        self.id = id
        self.name = name
        self.news = news
        self.start = start
        self.end = end
        self.stock = stock
        self.weight = weight
        self.quanpin = quanpin
        self.jianpin = jianpin
        self.valid = valid
        self.titles = titles
