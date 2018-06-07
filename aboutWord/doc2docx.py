# encoding=gbk


from win32com import client as wc
import os

word = wc.Dispatch('Word.Application')
# 后台运行，显示，不警告
word.Visible = False
word.DisplayAlerts = 0


def traverse(dirName=r'E:\python\Python27Project\aboutWord'):
    for root, dirs, files in os.walk(unicode(dirName, 'gbk')):
        for theFile in files:
            doc2docx(root, theFile)


def doc2docx(parentDir, fileName):
    try:
        if fileName.endswith('.doc'):
            fileFullPath = os.path.join(parentDir, fileName)
            print(fileFullPath)
            doc = word.Documents.Open(fileFullPath)
            doc.SaveAs(fileFullPath + 'x', 12)  # 17对应于下表中的pdf文件
            doc.Close()
            os.remove(fileFullPath)
    except Exception as e:
        print(e)
        print('另存为失败:' + fileName)


def quitWord():
    try:
        word.Quit()
    except:
        print('退出失败')


if "__main__" == __name__:
    # import sys
    #
    # reload(sys)
    # sys.setdefaultencoding('utf-8')
    try:
        rootDir = raw_input('请输入文件夹:')
        # traverse(rootDir)
        # quitWord()
    except Exception as e:
        raw_input('出了问题'+e.message)