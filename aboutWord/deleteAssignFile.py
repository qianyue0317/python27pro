# encoding=utf-8

import os


def deleteFiles(dirName):
    for root, dirs, files in os.walk(unicode(dirName, 'utf-8')):
        for theFile in files:
            if theFile.endswith('.doc'):
                os.remove(os.path.join(root, theFile))
    print('删除成功')


if "__main__" == __name__:
    deleteFiles(raw_input('请输入文件夹:'))
