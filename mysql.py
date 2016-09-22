#coding:utf-8
#-*- coding: UTF-8 -*- 。
#-------------------------------------------------------------------------------
# Name:        sql连接模块
# Purpose:
#
# Author:      zhangxin
#
# Created:     21/06/2016
# Copyright:   (c) Administrator 2016
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import MySQLdb

class MYSQL:
    def __init__(self):
        self.con = MySQLdb.connect(host='61.147.114.76',user='news',passwd='news',db='news',port=3306,charset='utf8')
        self.cursor = self.con.cursor()

    def close(self):
        self.cursor.close()
        self.con.close()
