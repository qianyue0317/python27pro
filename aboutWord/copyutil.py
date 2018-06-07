# encoding=utf-8

import shutil

def copy(sourceDir,targetDir):
    shutil.copy2(sourceDir,targetDir)


if '__main__' == __name__:
    copy(r'E:\python\Python27Project\aboutWord\0805000.files',r'E:\python\Python27Project\db')
