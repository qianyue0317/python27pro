# coding=utf-8

# 文件名：
# BatchConverWords2Html.py
# 说明：
# 批量将一个文件夹下的所有.doc/.docx文件转为.html文件，需要安装对应的win32模块
# 调用方式：进入源程序目录，命令：python BatchConverWords2Html.py RootDir

from win32com import client as wc
import os

word = wc.Dispatch('Word.Application')
# 后台运行，显示，不警告
word.Visible = False
word.DisplayAlerts = 0


def wordsToHtml(rootDir='', wordFileName=''):
    wordFullName = os.path.join(rootDir, wordFileName)
    doc = word.Documents.Open(wordFullName)

    if (wordFileName.endswith('.doc') or wordFileName.endswith('.docx')):
        fileName = wordFileName[:-5]
        htmlName = fileName + ".html"
        htmlFullName = os.path.join(rootDir, htmlName)
        # htmlFullName = unicode(path, "gbk") + "\\" + htmlName
        print "generate html:" + htmlFullName
        doc.SaveAs(htmlFullName, 10)
        doc.Close()
    print ""
    print "Finished!"


def quitWord():
    try:
        word.Quit()
    except Exception as e:
        print(e)
        print('退出word失败')


if __name__ == '__main__':
    import sys

    if sys.getdefaultencoding() != 'gbk':
        reload(sys)
        sys.setdefaultencoding('gbk')
    rootDir = raw_input('请输入根路径:')
    fileName = raw_input('请输入文件名:')
    wordsToHtml(rootDir, fileName)
