# encoding:gbk
# decoding:gbk
import os
import xlrd
import sys
reload(sys)
sys.setdefaultencoding("gbk")
fileDir = raw_input('请输入待解析表格全路径:')
fileTargetDir = raw_input('请输入目标文件夹:')
# fileName = r"C:\Users\abc\Desktop\3G缺失信息-修改.xlsx"
fileName = fileDir
print fileName
book = xlrd.open_workbook(fileName)

sheet_name = book.sheet_names()[0]
print sheet_name
sheet0 = book.sheet_by_name(sheet_name)

rowNum = sheet0.nrows
colNum = sheet0.ncols

cityValue = sheet0.col_values(1)
cityTemp = []
for i in cityValue:
    if cityValue.index(i) != 0 and not cityTemp.__contains__(i):
        cityTemp.append(i)

for i in cityTemp:
    print i
# lac
lacValues = sheet0.col_values(3)
# cell
cellValues = sheet0.col_values(4)
# 经度
jingValue = sheet0.col_values(5)
# 纬度
weiValue = sheet0.col_values(6)


x = 0
for i in cityTemp:
    k = -1
    x += 1
    # fileTemp = file(r'C:\Users\abc\Desktop'+os.sep+str(x)+'.txt','w')
    strTemp = str(i)
    # fileTemp = file(r'C:\Users\abc\Desktop'+os.sep+strTemp+'.txt','w')
    if not os.path.isdir(fileTargetDir):
        os.makedirs(fileTargetDir)
    fileTemp = file(fileTargetDir+os.sep+strTemp+'.txt','w')

    for y in cityValue:
        k += 1
        if i == y:
            mLacValue = int(lacValues[k])
            mCellValue = int(cellValues[k])
            mJingValue = jingValue[k]
            mWeiValue = weiValue[k]
            if mJingValue =='' or mWeiValue == '':
                continue
            fileTemp.write(str(mJingValue)+','+str(mWeiValue)+','+str(mCellValue)+','+str(mLacValue)+'\n')
