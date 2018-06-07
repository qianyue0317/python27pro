# -*- encoding:utf-8 -*-



from docx import Document
import sys
import re
import os



originStr = '''**
##D##
$$0000000$$
**
'''

styleName = "DefaultParagraph"

defaultencoding = 'utf-8'
if sys.getdefaultencoding() != defaultencoding:
    reload(sys)
    sys.setdefaultencoding(defaultencoding)

def dealFunc(root=r'E:\python\Python27Project\aboutWord',fileName= r'0805000.docx'):
    filePath = os.path.join(root,fileName)
    print('filePath是什么:'+filePath)
    try:
        myDoc = Document(filePath)
        index = 1
        for ps in myDoc.paragraphs:
            print (ps.text)
            styleName = ps.style.name
            if ps.text.startswith('答案：'):
                #print(ps.text)
                answer = re.findall('[A-D]', ps.text)
                #print (answer)
                if answer.count == 0: #防止越界
                    answer = ['']
                insertedStr = originStr.replace('0000000',fileName[0:7])
                insertedStr = insertedStr.replace('D',answer[0])
                ps.insert_paragraph_before(insertedStr,styleName)
            text = str(ps.text)
            matchstr = str(index) + '.' #题目序号
            print (matchstr)
            if text.startswith(matchstr):
                temp = index == 1 and ' ' or '++++\n'
                text = text.replace(matchstr,temp)
                ps.text = text
                index += 1
        newDir = os.path.join(root, fileName[0:7])
        os.mkdir(newDir)
        newFilePath = os.path.join(newDir, fileName[0:7]+'.docx')
        myDoc.save(newFilePath)
        index = 1
    except Exception as e:
        print(e)
        print('转换出问题的文件:'+filePath)


if '__main__' == __name__:
    dealFunc()
