# -*- coding: utf-8 -*-
# -------------------------------------------------------------------------------
# Name:        历史时间转时间戳 模块
# Purpose:
#
# Author:      zhangxin
#
# Created:     12/09/2016
# Copyright:   (c) Administrator 2016
# Licence:     <your licence>
# -------------------------------------------------------------------------------

import time


def time_stamp(time_give):

    old_time_date = time.strptime(time_give, "%Y-%m-%d %H:%M:%S")

    old_time_date_stamp = time.mktime(old_time_date)

    return int(old_time_date_stamp*1000)


if __name__ == "__main__":
    print time_stamp('2016-10-12 8:00:00')
    print time_stamp('2016-10-13 8:00:00')
