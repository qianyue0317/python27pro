# -*- encoding:utf-8 -*-


import sys
import os

from aboutWord.convertWord2html import quitWord
from aboutWord.dealWord import dealFunc

defaultencoding = 'utf-8'
if sys.getdefaultencoding() != defaultencoding:
    reload(sys)
    sys.setdefaultencoding(defaultencoding)


def func1(dirName):
    for root, parent, files in os.walk(unicode(dirName, 'utf-8')):
        for fileName in files:
            if fileName.endswith('.docx') and not fileName.startswith('~$'):
                # print('开始转换')
                dealFunc(root, fileName)


if '__main__' == __name__:
    while True:
        rootDir = raw_input('input Root Dir:')
        func1(rootDir)
        quitWord()
        print('finish')
