# coding:utf-8
# -*- coding: UTF-8 -*- 。
# -------------------------------------------------------------------------------
# Name:        主界面模块
# Purpose:
#
# Author:      zhangxin
#
# Created:     12/09/2016
# Copyright:   (c) Administrator 2016
# Licence:     <your licence>
# -------------------------------------------------------------------------------
from PyQt4 import QtCore, QtGui
import sys
import run


def main():
    # 显示主页面
    app = QtGui.QApplication(sys.argv)
    win = run.Run_2_content_Form()
    win.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
