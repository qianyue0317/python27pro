# encoding:utf-8

# from uiautomator import device
# import unittest
# import time

# 导入此程序所需的monkeyrunner模块

from com.android.monkeyrunner import MonkeyRunner, MonkeyDevice

# 连接当前设备，返回一个MonkeyDevice对象

device = MonkeyRunner.waitForConnection()

# device.drag((100, 300), (500, 300), 0.1, 5)

device.type('18201349877')
device.touch(300, 1150, MonkeyDevice.DOWN_AND_UP)
# device.press('KEYCODE_HOME','DOWN_AND_UP')
device.press('KEYCODE_DPAD_DOWN', 'DOWN_AND_UP')
device.type('12345678')
device.press('KEYCODE_DPAD_DOWN', 'DOWN_AND_UP')

# 运行测试应用
device.startActivity(component="com.zcjy.primaryzsd.debug/com.zcjy.primaryzsd.debug.app.main.GuideActivity")

# MonkeyRunner.alert('test dialog')

# device.reboot()
print('success')
# 形成一个点击事件

# device.touch(200, 1800, 'DOWN_AND_UP')

# 截取屏幕截图

# result = device.takeSnapshot()

# 将截图保存至文件

# result.writeToFile(r'E:\python\Python27Project\aboutAndroid\shot1.png', 'png')
