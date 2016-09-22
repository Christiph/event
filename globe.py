#coding:utf-8
#-*- coding: UTF-8 -*- 。
#-------------------------------------------------------------------------------
# Name:        全局变量模块
# Purpose:
#
# Author:      zhangxin
#
# Created:     21/06/2016
# Copyright:   (c) Administrator 2016
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import MySQLdb

# 保存所有的事件实体对象
events_array = []

# 当前事件在events_array中的index
current_index = 0

# 当前事件所有参数 (id, name, news, start, end, stock, weight, quanpin, jianpin, valid, newsTitles)
ID = -1
name = ''
news = ''
valid = ''
news_titles = u"相关新闻如下:"

# 时间戳
time = 0            # 当前系统时间戳  1456848000000
time_seven = 0      # 7天之前的时间戳

# 配置参数
delete_path = "D:\\[8]RunEvent\\out\\delete.txt"
update_path = "D:\\[8]RunEvent\\out\\update.txt"

# 默认7天
seven = 300

# 删除标记
flag_delete = False

# 干预历史数据
time_start_old = 1463241600000       # 4月1号的时间戳
time_end_old = 1463846400000         # 4月16号的时间戳

# 全局变量初始化
def clear(self):
    self.events_array = []
    self.current_index = 0
    self.news_titles = u"相关新闻如下:"
    self.ID = -1
    self.name = ''
    self.news = ''
    self.valid = ''
