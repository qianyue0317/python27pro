# encoding=gbk
import zipfile
import os


def zip(dirName):
    z = zipfile.ZipFile(os.path.split(dirName)[1]+'.zip', 'w', zipfile.ZIP_DEFLATED)
    for dirpath, dirnames, filenames in os.walk(dirName):
        for filename in filenames:
            if not filename.endswith('.zip'):
                print('正在压缩文件:'+filename)
                z.write(os.path.join(dirpath, filename))
    z.close()
    print('压缩完毕')


if '__main__' == __name__:
    zip(r'E:\python\Python27Project\aboutWord')