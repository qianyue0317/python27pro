# encoding=utf-8

import sys
import os
from docx import Document

reload(sys)
sys.setdefaultencoding('utf-8')


rootDir = r'C:\Users\Administrator\Desktop\初中版-评测题\test\0406000第6章实数综合.docx'
saveAsDir = r'C:\Users\Administrator\Desktop\初中版-评测题\test\0406000.docx'



myDoc = Document(unicode(rootDir, 'utf-8'))
for pg in myDoc.paragraphs:
    print(pg.text)
    if pg.text.startswith('2'):
        pg.runs[0].text = ""
        pg.insert_paragraph_before("++++")
        # print(pg.runs[0].text)
        # pg.runs.remove(pg.runs[0])
    # print(pg.text)
