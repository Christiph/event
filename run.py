# -*- coding: utf-8 -*-
# coding:utf-8
# -------------------------------------------------------------------------------
# Name:        主功能模块
# Purpose:
#
# Author:      zhangxin
#
# Created:     12/09/2016
# Copyright:   (c) Administrator 2016
# Licence:     <your licence>
# -------------------------------------------------------------------------------
import time
import event
from PyQt4 import QtCore, QtGui
import sys
import globe
import writer
import mysql
from PyQt4.QtGui import QMessageBox

# 及其关键的两行代码，造成全部乱码
reload(sys)
sys.setdefaultencoding('utf8')

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8


    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)


class Run_2_content_Form(QtGui.QMainWindow):
    def __init__(self):
        super(Run_2_content_Form, self).__init__()
        self.setup_ui(self)
        self.retranslate_ui(self)
        # globe.time = "%d" % (time.time() * 1000)
        seven = 60 * 60 * 1000 * 24L * long(globe.seven)
        globe.time_seven = long(globe.time) - seven
        self.wr = writer.Writer(globe.update_path)
        self.wr_delete = writer.Writer(globe.delete_path)
        self.mysql_conn = mysql.MYSQL()

    def setup_ui(self, dialog):

        dialog.setObjectName(_fromUtf8("dialog"))
        dialog.resize(657, 853)
        self.label = QtGui.QLabel(dialog)
        self.label.setGeometry(QtCore.QRect(20, 80, 81, 31))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(dialog)
        self.label_2.setGeometry(QtCore.QRect(20, 130, 81, 31))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.num = QtGui.QTextEdit(dialog)
        self.num.setGeometry(QtCore.QRect(70, 80, 101, 31))
        self.num.setObjectName(_fromUtf8("num"))
        self.title = QtGui.QTextEdit(dialog)
        self.title.setGeometry(QtCore.QRect(70, 130, 361, 31))
        self.title.setObjectName(_fromUtf8("title"))
        self.label_3 = QtGui.QLabel(dialog)
        self.label_3.setGeometry(QtCore.QRect(20, 170, 81, 31))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.content = QtGui.QTextEdit(dialog)
        self.content.setGeometry(QtCore.QRect(70, 180, 571, 500))
        self.content.setObjectName(_fromUtf8("content"))

        # 跳转框
        self.index = QtGui.QTextEdit(dialog)
        self.index.setGeometry(QtCore.QRect(500, 130, 50, 31))
        self.index.setObjectName(_fromUtf8("index"))

        # 跳转按钮
        self.button_index = QtGui.QPushButton(dialog)
        self.button_index.setGeometry(QtCore.QRect(570, 130, 50, 31))
        self.button_index.setObjectName(_fromUtf8("button_index"))

        # 事件状态栏
        self.label_4 = QtGui.QLabel(dialog)
        self.label_4.setGeometry(QtCore.QRect(200, 80, 80, 31))
        self.label_4.setObjectName(_fromUtf8("label_4"))

        self.label_5 = QtGui.QLabel(dialog)
        self.label_5.setGeometry(QtCore.QRect(280, 80, 400, 31))
        self.label_5.setObjectName(_fromUtf8("label_5"))

        self.label_6 = QtGui.QLabel(dialog)
        self.label_6.setGeometry(QtCore.QRect(500, 80, 100, 31))
        self.label_6.setObjectName(_fromUtf8("label_5"))

        # 上一篇
        self.button_last = QtGui.QPushButton(dialog)
        self.button_last.setGeometry(QtCore.QRect(70, 700, 75, 45))
        self.button_last.setObjectName(_fromUtf8("button_last"))

        # 下一篇
        self.Button_next = QtGui.QPushButton(dialog)
        self.Button_next.setGeometry(QtCore.QRect(180, 700, 75, 45))
        self.Button_next.setObjectName(_fromUtf8("Button_next"))

        # 一键删除
        self.button_delete = QtGui.QPushButton(dialog)
        self.button_delete.setGeometry(QtCore.QRect(60, 20, 85, 35))
        self.button_delete.setObjectName(_fromUtf8("button_delete"))

        # 开始干预
        self.button_do = QtGui.QPushButton(dialog)
        self.button_do.setGeometry(QtCore.QRect(180, 20, 85, 35))
        self.button_do.setObjectName(_fromUtf8("button_do"))

        # 修改主题
        self.button_update = QtGui.QPushButton(dialog)
        self.button_update.setGeometry(QtCore.QRect(450, 700, 75, 45))
        self.button_update.setObjectName(_fromUtf8("button_update"))

        # 无效删除
        self.button_delete_current = QtGui.QPushButton(dialog)
        self.button_delete_current.setGeometry(QtCore.QRect(560, 700, 75, 45))
        self.button_delete_current.setObjectName(_fromUtf8("button_delete_current"))

        self.retranslate_ui(dialog)
        QtCore.QObject.connect(self.button_delete, QtCore.SIGNAL(_fromUtf8("clicked()")), self.one_delete)
        QtCore.QObject.connect(self.button_do, QtCore.SIGNAL(_fromUtf8("clicked()")), self.read_all_events)
        QtCore.QObject.connect(self.button_last, QtCore.SIGNAL(_fromUtf8("clicked()")), self.last_event)
        QtCore.QObject.connect(self.Button_next, QtCore.SIGNAL(_fromUtf8("clicked()")), self.next_event)
        QtCore.QObject.connect(self.button_delete_current, QtCore.SIGNAL(_fromUtf8("clicked()")), self.delete)
        QtCore.QObject.connect(self.button_update, QtCore.SIGNAL(_fromUtf8("clicked()")), self.update)
        QtCore.QObject.connect(self.button_index, QtCore.SIGNAL(_fromUtf8("clicked()")), self.search)
        QtCore.QMetaObject.connectSlotsByName(dialog)

    def retranslate_ui(self, dialog):
        dialog.setWindowTitle(_translate("dialog", "事件人工干预软件", None))
        self.label.setText(_translate("dialog", "事件ID", None))
        self.label_2.setText(_translate("dialog", "事件主题", None))
        self.label_3.setText(_translate("dialog", "相关新闻", None))
        self.button_last.setText(_translate("dialog", "上一事件", None))
        self.Button_next.setText(_translate("dialog", "下一事件", None))
        self.button_delete.setText(_translate("dialog", "一键删除", None))
        self.button_do.setText(_translate("dialog", "开始干预", None))
        self.button_update.setText(_translate("dialog", "修改主题", None))
        self.button_delete_current.setText(_translate("dialog", "无效删除", None))
        self.button_index.setText(_translate("dialog", "跳转", None))

    # 一键删除
    def one_delete(self):
        customMsgBox = QMessageBox(self)
        customMsgBox.setWindowTitle("Custom message box")

        okButton = customMsgBox.addButton(unicode("确定"),QMessageBox.ActionRole)
        cancelButton = customMsgBox.addButton(unicode("取消"), QMessageBox.ActionRole)

        customMsgBox.setText(unicode("确定一键删除么？"))
        customMsgBox.exec_()

        button = customMsgBox.clickedButton()
        if button == okButton:
            try:
                self.delete_no_use()   # 执行一键删除
            except Exception, ex:
                print "[连接中断] ", ex, " 已重新建立连接"
                self.mysql_conn = mysql.MYSQL()
                self.delete_no_use()  # 执行一键删除
            self.content.setText(unicode("无效事件已剔除！"))
        elif button == cancelButton:
            self.content.setText(unicode("已取消！"))

    # 一键删除过期无效事件
    def delete_no_use(self):

        # 数据库备份
        self.mysql_conn.cursor.execute('Drop TABLE IF EXISTS events_total_backup_ZX')
        self.mysql_conn.cursor.execute('CREATE TABLE IF NOT EXISTS events_total_backup_ZX SELECT * FROM events_total')

        # 本地备份
        sql = "select id,event_name,related_news,is_valid FROM events_total where end_time < %s " % globe.time_seven
        self.mysql_conn.cursor.execute(sql)
        result = self.mysql_conn.cursor.fetchall()

        ids = []
        for r in result:
            temp = r[2].split("\t")
            if r[3] == -1 or len(temp) == 1:
                self.wr_delete.wr(unicode(str(r[0]) + "##" + str(r[1]) + "##" + str(r[2]) + "\n"))
                self.wr_delete.flush()
                ids.append(unicode(r[0]))

        self.wr_delete.close()

        # 一键删除
        id_delete = "','".join(ids)
        sql = "DELETE FROM events_total where id in ('%s')" % id_delete

        self.mysql_conn.cursor.execute(sql)
        self.mysql_conn.con.commit()   # commit 提交修改

    # 读取所有事件（潜在事件或者有效事件）  events_total  events_total
    def read_all_events(self):

        # 全局变量初始化
        globe.clear(globe)

        # 读取MySQL中的事件: valid 为0或1，且七天以内，且新闻数大于1
        self.mysql_conn.cursor.execute(
            # "select * from events_total where is_valid >= 0 and end_time > %s " % globe.time_seven + " ORDER BY id asc")
            "select * from events_total where is_valid >= 0 and end_time > %s and end_time < %s " % (globe.time_start_old, globe.time_end_old) + " ORDER BY id asc")

        # 数据读取
        results = self.mysql_conn.cursor.fetchall()
        for r in results:

            # Event(id, name, news, start, end, stock, weight, quanpin, jianpin, valid, titles)
            temp = r[2].split("\t")
            if len(temp) > 4:
                ev = event.Event(r[0], r[1], r[2], r[3], r[4], r[5], r[6], r[7], r[8], r[9], u'保留变量')
                globe.events_array.append(ev)

        # 数据填充：填入第一个事件的相关数据
        if len(globe.events_array) > 0:
            n = globe.events_array[0]
            self.fill_data(n)
            self.label_6.setText(unicode(str(1) + " / " + str(len(globe.events_array))))
            globe.current_index = 0   # 设置当前事件的index

    # 下一个事件
    def next_event(self):

        # 清空 globe.news_titles
        globe.news_titles = ""

        if globe.current_index + 1 < len(globe.events_array):
            n = globe.events_array[globe.current_index + 1]
            self.fill_data(n)
            self.label_6.setText(unicode(str(globe.current_index + 2) + " / " + str(len(globe.events_array))))
            globe.current_index += 1
        else:
            self.label_5.setText(unicode("下一篇没有了！"))

            if globe.flag_delete:
                globe.flag_delete = False
                n = globe.events_array[globe.current_index]
                self.fill_data(n)
                self.label_6.setText(unicode(str(globe.current_index + 1) + " / " + str(len(globe.events_array))))

    # 上一个事件
    def last_event(self):

        # 清空 globe.news_titles
        globe.news_titles = ""

        if globe.current_index - 1 >= 0:

            n = globe.events_array[globe.current_index - 1]
            self.fill_data(n)
            self.label_6.setText(unicode(str(globe.current_index) + " / " + str(len(globe.events_array))))
            globe.current_index -= 1

        else:
            self.label_5.setText(unicode("上一篇没有了！"))

    # 当前事件无效删除
    def delete(self):

        try:

            self.mysql_conn.cursor.execute("update events_total set is_valid = -1 where id = %s " % globe.ID)
            self.mysql_conn.con.commit()

            temp = globe.events_array[globe.current_index]
            globe.events_array = filter(lambda x: x != temp, globe.events_array)
            globe.current_index -= 1

            globe.flag_delete = True
            self.next_event()  # 跳转到下一个事件

        except Exception, ex:
            print "[连接中断] ", ex, " 已重新建立连接"
            self.mysql_conn = mysql.MYSQL()
            temp = globe.events_array[globe.current_index]
            globe.events_array = filter(lambda x: x != temp, globe.events_array)
            globe.current_index -= 1

            self.mysql_conn.cursor.execute("update events_total set is_valid = -1 where id = %s " % globe.ID)
            self.mysql_conn.con.commit()
            globe.flag_delete = True
            self.next_event()  # 跳转到下一个事件

    # 修改主题名称，同时将valid值置为1
    def update(self):

        title = str(self.title.toPlainText())

        if title == "":
            self.label_5.setText(unicode("有效事件的标题不能为空！！"))
        else:

            temp = globe.events_array[globe.current_index]
            temp.name = title
            temp.valid = 1
            globe.events_array[globe.current_index] = temp

            self.wr.wr(unicode(str(globe.ID) + "\t" + title + "\t" + "1\n"))
            self.wr.flush()

            # 跳转到下一个事件
            self.next_event()

    def search(self):

        # 清空 globe.news_titles
        globe.news_titles = ""

        index = int(self.index.toPlainText())

        if index > 0:
            n = globe.events_array[index - 1]
            self.fill_data(n)
            self.label_6.setText(unicode(str(index) + " / " + str(len(globe.events_array))))
            globe.current_index = index - 1

            # 清空跳转框
            self.index.setText(unicode(""))
        else:
            self.label_5.setText(unicode("index不可以为 0 ！"))
            self.index.setText(unicode(""))

    # 查询相关新闻标题
    def get_news_title(self):

        try:
            temp = globe.news
            urls = temp.split("\t")
            urlall = "','".join(urls)

            self.mysql_conn.cursor.execute("select title from news_info where url in ('%s')" % urlall)

            # 数据读取
            count = 1
            results = self.mysql_conn.cursor.fetchall()
            for r in results:
                globe.news_titles = globe.news_titles + "\n[" + str(count) + "] 《" + r[0] + "》"
                count += 1

        except Exception, ex:
            print "[连接中断]", ex, " 已重新建立连接"
            self.mysql_conn = mysql.MYSQL()     # 重新建立连接
            temp = globe.news
            urls = temp.split("\t")
            urlall = "','".join(urls)

            self.mysql_conn.cursor.execute("select title from news_info where url in ('%s')" % urlall)

            # 数据读取
            count = 1
            results = self.mysql_conn.cursor.fetchall()
            for r in results:
                globe.news_titles = globe.news_titles + "\n[" + str(count) + "] 《" + r[0] + "》"
                count += 1

    # 数据填充
    def fill_data(self, n):

        # 查询相关新闻
        globe.news = n.news
        self.get_news_title()

        # 填充事件信息栏
        self.num.setText(str(n.id))
        self.title.setText(unicode(n.name))
        self.content.setText(unicode(globe.news_titles))

        # 设置状态栏
        self.label_4.setText(unicode("ISVALID：" + str(n.valid)))

        if n.valid > 0:
            self.label_5.setText(unicode("当前状态： 有效！"))
        else:
            self.label_5.setText(unicode("当前状态： 潜在事件！"))

        globe.ID = n.id  # 保存当前事件ID