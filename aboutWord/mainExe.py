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
    for root, parent, files in os.walk(dirName):
        for fileName in files:
            if fileName.endswith('.docx') and not fileName.startswith('~$'):
                # print('开始转换')
                try:
                    dealFunc(root, fileName)
                except Exception as e:
                    print('出问题的文件是:'.encode(encoding='gbk')+os.path.join(root,fileName))

if '__main__' == __name__:
    while True:
        rootDir = raw_input('input Root Dir:')
        func1(rootDir)
        quitWord()
        print('finish')