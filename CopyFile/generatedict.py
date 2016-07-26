# encoding:utf-8
import sys

fileName = r'C:\Users\abc\Desktop\zip.txt'
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9',':','\\','/','.',',','!','~','#','@','$','(',')','_','-','=','+']
digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
file = open(fileName, 'w')
print len(letters)
lenth = len(letters)
passwordletters=[]
password = ''
for a in range(0,lenth):
    file.write(letters[a]+'\n')
    for b in range(0,lenth):
        file.write(letters[a]+letters[b]+'\n')
        for c in range(0,lenth):
            file.write(letters[a]+letters[b]+letters[c]+'\n')
            # for d in range(0,lenth):
            #     file.write(letters[a]+letters[b]+letters[c]+letters[d]+'\n')
            #     for e in range(0,lenth):
            #         file.write(letters[a]+letters[b]+letters[c]+letters[d]+letters[e]+'\n')