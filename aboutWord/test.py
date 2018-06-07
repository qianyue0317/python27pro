# -*- encoding:utf-8 -*-
import win32com
from win32com.client import Dispatch, constants
wordApp = win32com.client.DispatchEx('Word.Application')

# 后台运行，显示，不警告
wordApp.Visible = False
wordApp.DisplayAlerts = 0

# 创建新的文档
# doc = wordApp.Documents.Add()
doc = wordApp.Documents.open('E:/python/Python27Project/aboutWord/0805000.docx')

# 插入文字
doc.Paragraphs.Last.Range.Text = 'hello!'

# 保存文件
doc.SaveAs('d://say_hello.docx')

# doc.close()