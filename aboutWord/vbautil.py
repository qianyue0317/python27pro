# encoding=utf-8

# import win32com.client
# word=win32com.client.Dispatch("Word.Application")
# word.Workbooks.Open(Filename="***.xls")
# ret = word.Application.Run("foo")
# print ret
# xls.Application.Quit()

from win32com import client as wc
import os
word = wc.Dispatch('Word.Application')
# 后台运行，显示，不警告
word.Visible = False
word.DisplayAlerts = 0

doc = word.Documents.Open(r'E:\python\Python27Project\aboutWord\0806102.docx')
run = word.Application.Run('changeIndex2text',[])
print(run)
word.Application.Quit()