# -*- encoding:utf-8 -*-
# create by Administrator on 2018/6/29
# 动态导入功能 通过字符串导入模块

from importlib import import_module


def dynamic_import(module):
    return import_module(module)


if '__main__' == __name__:
    module = dynamic_import('config')
    print(module.a)
    pass
