# -*- encoding:utf-8 -*-
# create by Administrator on 2018/6/21

from celery import Celery

celery = Celery('thecelery', include=['celeryContainer.tasks'], broker='redis://localhost:6379')
