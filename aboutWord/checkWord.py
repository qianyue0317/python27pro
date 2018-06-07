# encoding=utf-8

import sys
import os
from docx import Document
import re

reload(sys)
sys.setdefaultencoding('utf-8')

invalidateDoc = []


# 检查一个word中
def checkWord(rootDir='', fileName=''):
    fileFullName = os.path.join(rootDir, fileName)

    print(fileFullName)
    if fileFullName.endswith('.docx') and not fileName.startswith('~$'):
        myDoc = Document(fileFullName)
        paragraphs = myDoc.paragraphs
        plusList = 0
        otherMark = 0

        for pg in paragraphs:
            # if pg.text.find('++++'):
            if re.findall('\+\+\+\+', pg.text):
                plusList += 1
                print("index:" + pg.text)
            if re.findall('\#\#[A-D]\#\#', pg.text):
                # if pg.text.find('$$'):
                otherMark += 1
                print('answer:' + pg.text)
        print('加号数量:' + str(plusList))
        print('答案数量:' + str(otherMark))
        if plusList == 0 and otherMark == 0:
            return
        if plusList != otherMark - 1:
            invalidateDoc.append(fileName)


def traverse(rootDir=''):
    for root, parents, files in os.walk(unicode(rootDir, 'utf-8')):
        # for root, parents, files in os.walk(rootDir):
        for theFile in files:
            checkWord(root, theFile)


if '__main__' == __name__:
    rootFolder = raw_input('请输入文件夹:')
    traverse(rootFolder)
    print('不合格的word:')
    print(invalidateDoc)
    print('不合格的数量:' + str(len(invalidateDoc)))
