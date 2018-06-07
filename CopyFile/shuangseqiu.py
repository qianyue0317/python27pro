# encoding:gbk
import random
import thread
redResult = []
greenResult = 0
i=0
while True:
    redTemp = random.randint(1,33)
    if not redTemp in redResult:
        redResult.append(redTemp)
        i+=1
    if i == 6:
        greenResult = random.randint(1,16)
        break
redResult.sort()
print "红球:",redResult," 蓝球:",greenResult