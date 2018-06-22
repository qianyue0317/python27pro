# -*- encoding:utf-8 -*-
# create by Administrator on 2018/6/21

from mycelery import celery
import time
import os


@celery.task
def helloCelery():
    print('pid:%s' % os.getpid())
    time.sleep(3)
    with open(r'./celery.txt', 'w') as tempFile:
        tempFile.write("你好")

    print('hello celery')
