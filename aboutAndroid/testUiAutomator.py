# encoding:utf-8
from uiautomator import device

# device.screen.on()
print('准备打印')
device.click(80, 150)
print(device.info)
print('打印完成')
