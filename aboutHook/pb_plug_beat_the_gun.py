# -*- encoding:utf-8 -*-
# create by Administrator on 2018/6/29


import pythoncom
import pyHook
import win32api
import win32con
import time
import threading
import random
import pyautogui
import sys

reload(sys)
sys.setdefaultencoding('utf-8')


def send_click():
    global down_num, up_num
    while True:
        if down_num != up_num:
            pyautogui.moveRel(None, 100, 1)
            print 'click ok'


flag = True


def mouse_move_down():
    global flag
    while flag:
        pyautogui.moveRel(None, 3)
        time.sleep(0.01)


def onMouse_leftdown(event):
    # 监听鼠标左键按下事件
    global flag
    flag = True
    threading.Thread(target=mouse_move_down).start()
    global down_num
    down_num += 1
    print "left DOWN DOWN" + str(down_num)
    return True
    # 返回 True 表示响应此事件，False表示拦截


def onMouse_leftup(event):
    # 监听鼠标左键弹起事件
    global flag
    flag = False
    global up_num
    up_num += 1
    print "left UP UP UP" + str(up_num)
    return True


def main():
    print('开始hook')
    hm = pyHook.HookManager()
    hm.MouseLeftDown = onMouse_leftdown
    hm.MouseLeftUp = onMouse_leftup
    hm.HookMouse()
    # 进入循环，如不手动关闭，程序将一直处于监听状态
    pythoncom.PumpMessages()


if __name__ == "__main__":
    down_num = 0
    up_num = 0
    # 新线程执行的代码:
    # print('thread %s is running...' % threading.current_thread().name)
    # t = threading.Thread(target=send_click, name='sendThread')
    # t.start()
    # t.join()
    main()
