# coding:utf-8
# "============================================="
# "[*]Android lockscreen(gesture) cracker"
# "[*]Updated by obaby QQ:289090351"
# "[*]Mars Information Security"
# "[*]http://www.h4ck.org.cn"
# "[*]coding by g0t3n update by obaby
# "============================================="



import sys
import os
import hashlib
import struct
import binascii
from copy import deepcopy

filehandle = None
db = "./hash.db"
init_mapper = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
mapper_queue = []  # tmp_mapper,startx,starty,prev_path
key_mapper = [['\x00', '\x01', '\x02'], ['\x03', '\x04', '\x05'], ['\x06', '\x07', '\x08']]


def notfull(mapper):
    for x in range(3):
        for y in range(3):
            if (mapper[x][y] != 0):
                return True
    return False


# 因为必须两个以上九个以下
def canwritelog(mapper):
    cnt = 0
    for x in range(3):
        for y in range(3):
            if mapper[x][y] == 1:
                cnt += 1
            if cnt > 2:
                return True
    return False


def writelog(tmp, prev):
    strings = ""
    paths = ""
    for i in prev:
        x, y = i
        paths = paths + str(x) + str(y)
        strings = strings + key_mapper[x][y]
    # print "writelog: strings => "+strings + " | " +hashlib.sha1(strings).hexdigest()
    filehandle.write(paths + " | " + hashlib.sha1(strings).hexdigest() + '\n')


def generatehashtable():
    print "[*]Generate hash.db .........\n[*]Waiting..............."
    rounds = 1
    for startxs in range(3):
        for startys in range(3):
            # start point to 0,0
            # startx,starty = 0,0
            cur_mapper = init_mapper
            init = 0
            prev_path = []

            startx, starty = startxs, startys
            while (True):

                if init == 0:  # init
                    tmp_mapper = deepcopy(cur_mapper)  # u r not virgin
                    tmp_mapper[startx][starty] = 1
                    prev_path.append((startx, starty))
                    init = 1
                else:
                    if len(mapper_queue) == 0:  # 队列为空证明finish了
                        break
                    tmp_mapper, startx, starty, prev_path = mapper_queue.pop()
                # print "head => "+repr(tmp_mapper)
                # print "mapper_queue =>"+repr(mapper_queue)
                if (startx + 1 < 3):  # right
                    tmp = deepcopy(tmp_mapper)
                    tmp_prev_path = deepcopy(prev_path)
                    tmp_prev_path.append((startx + 1, starty))
                    if (tmp_mapper[startx + 1][starty] != 1):  # 如果该点本来为 1,即结束,即不再入栈
                        tmp[startx + 1][starty] = 1
                        mapper_queue.append((tmp, startx + 1, starty, tmp_prev_path))
                    if canwritelog(tmp):
                        writelog(tmp, tmp_prev_path)  # !!!

                if (startx - 1 >= 0):  # left
                    tmp = deepcopy(tmp_mapper)
                    tmp_prev_path = deepcopy(prev_path)
                    tmp_prev_path.append((startx - 1, starty))
                    if (tmp_mapper[startx - 1][starty] != 1):
                        tmp[startx - 1][starty] = 1
                        mapper_queue.append((tmp, startx - 1, starty, tmp_prev_path))
                    if canwritelog(tmp):
                        writelog(tmp, tmp_prev_path)  # !!!

                if (starty + 1 < 3):  # down
                    tmp = deepcopy(tmp_mapper)

                    tmp_prev_path = deepcopy(prev_path)
                    tmp_prev_path.append((startx, starty + 1))
                    if (tmp_mapper[startx][starty + 1] != 1):
                        tmp[startx][starty + 1] = 1
                        mapper_queue.append((tmp, startx, starty + 1, tmp_prev_path))
                    if canwritelog(tmp):
                        writelog(tmp, tmp_prev_path)  # !!!

                if (starty - 1 >= 0):  # up
                    tmp = deepcopy(tmp_mapper)

                    tmp_prev_path = deepcopy(prev_path)
                    tmp_prev_path.append((startx, starty - 1))
                    if (tmp_mapper[startx][starty - 1] != 1):
                        tmp[startx][starty - 1] = 1
                        mapper_queue.append((tmp, startx, starty - 1, tmp_prev_path))
                    if canwritelog(tmp):
                        writelog(tmp, tmp_prev_path)  # !!!
                # 斜 一位
                if (startx + 1 < 3) and (starty + 1 < 3):  # right down
                    tmp = deepcopy(tmp_mapper)

                    tmp_prev_path = deepcopy(prev_path)
                    tmp_prev_path.append((startx + 1, starty + 1))
                    if (tmp_mapper[startx + 1][starty + 1] != 1):
                        tmp[startx + 1][starty + 1] = 1
                        mapper_queue.append((tmp, startx + 1, starty + 1, tmp_prev_path))
                    if canwritelog(tmp):
                        writelog(tmp, tmp_prev_path)  # !!!
                if (startx - 1 >= 0) and (starty + 1 < 3):  # left down
                    tmp = deepcopy(tmp_mapper)
                    tmp_prev_path = deepcopy(prev_path)
                    tmp_prev_path.append((startx - 1, starty + 1))
                    if (tmp_mapper[startx - 1][starty + 1] != 1):
                        tmp[startx - 1][starty + 1] = 1
                        mapper_queue.append((tmp, startx - 1, starty + 1, tmp_prev_path))
                    if canwritelog(tmp):
                        writelog(tmp, tmp_prev_path)  # !!!

                if (startx - 1 >= 0) and (starty - 1 >= 0):  # left up
                    tmp = deepcopy(tmp_mapper)
                    tmp_prev_path = deepcopy(prev_path)
                    tmp_prev_path.append((startx - 1, starty - 1))
                    if (tmp_mapper[startx - 1][starty - 1] != 1):
                        tmp[startx - 1][starty - 1] = 1
                        mapper_queue.append((tmp, startx - 1, starty - 1, tmp_prev_path))
                    if canwritelog(tmp):
                        writelog(tmp, tmp_prev_path)  # !!!

                if (startx + 1 < 3) and (starty - 1 >= 0):  # right up
                    tmp = deepcopy(tmp_mapper)

                    tmp_prev_path = deepcopy(prev_path)
                    tmp_prev_path.append((startx + 1, starty - 1))
                    if (tmp_mapper[startx + 1][starty - 1] != 1):
                        tmp[startx + 1][starty - 1] = 1
                        mapper_queue.append((tmp, startx + 1, starty - 1, tmp_prev_path))
                    if canwritelog(tmp):
                        writelog(tmp, tmp_prev_path)  # !!!
                # 斜 两位
                if (startx + 1 < 3) and (starty + 2 < 3):
                    tmp = deepcopy(tmp_mapper)
                    tmp_prev_path = deepcopy(prev_path)
                    tmp_prev_path.append((startx + 1, starty + 2))
                    if (tmp_mapper[startx + 1][starty + 2] != 1):
                        tmp[startx + 1][starty + 2] = 1
                        mapper_queue.append((tmp, startx + 1, starty + 2, tmp_prev_path))
                    if canwritelog(tmp):
                        writelog(tmp, tmp_prev_path)  # !!!
                if (startx - 1 >= 0) and (starty + 2 < 3):
                    tmp = deepcopy(tmp_mapper)
                    tmp_prev_path = deepcopy(prev_path)
                    tmp_prev_path.append((startx - 1, starty + 2))
                    if (tmp_mapper[startx - 1][starty + 2] != 1):
                        tmp[startx - 1][starty + 2] = 1
                        mapper_queue.append((tmp, startx - 1, starty + 2, tmp_prev_path))
                    if canwritelog(tmp):
                        writelog(tmp, tmp_prev_path)  # !!!
                if (startx + 1 < 3) and (starty - 2 >= 0):
                    tmp = deepcopy(tmp_mapper)
                    tmp_prev_path = deepcopy(prev_path)
                    tmp_prev_path.append((startx + 1, starty - 2))
                    if (tmp_mapper[startx + 1][starty - 2] != 1):
                        tmp[startx + 1][starty - 2] = 1
                        mapper_queue.append((tmp, startx + 1, starty - 2, tmp_prev_path))
                    if canwritelog(tmp):
                        writelog(tmp, tmp_prev_path)  # !!!
                if (startx - 1 >= 0) and (starty - 2 >= 0):
                    tmp = deepcopy(tmp_mapper)
                    tmp_prev_path = deepcopy(prev_path)
                    tmp_prev_path.append((startx - 1, starty - 2))
                    if (tmp_mapper[startx - 1][starty - 2] != 1):
                        tmp[startx - 1][starty - 2] = 1
                        mapper_queue.append((tmp, startx - 1, starty - 2, tmp_prev_path))
                    if canwritelog(tmp):
                        writelog(tmp, tmp_prev_path)  # !!!

                if (startx + 2 < 3) and (starty + 1 < 3):
                    tmp = deepcopy(tmp_mapper)
                    tmp_prev_path = deepcopy(prev_path)
                    tmp_prev_path.append((startx + 2, starty + 1))
                    if (tmp_mapper[startx + 2][starty + 1] != 1):
                        tmp[startx + 2][starty + 1] = 1
                        mapper_queue.append((tmp, startx + 2, starty + 1, tmp_prev_path))
                    if canwritelog(tmp):
                        writelog(tmp, tmp_prev_path)  # !!!
                if (startx + 2 < 3) and (starty - 1 >= 0):
                    tmp = deepcopy(tmp_mapper)
                    tmp_prev_path = deepcopy(prev_path)
                    tmp_prev_path.append((startx + 2, starty - 1))
                    if (tmp_mapper[startx + 2][starty - 1] != 1):
                        tmp[startx + 2][starty - 1] = 1
                        mapper_queue.append((tmp, startx + 2, starty - 1, tmp_prev_path))
                    if canwritelog(tmp):
                        writelog(tmp, tmp_prev_path)  # !!!
                if (startx - 2 >= 0) and (starty - 1 >= 0):
                    tmp = deepcopy(tmp_mapper)
                    tmp_prev_path = deepcopy(prev_path)
                    tmp_prev_path.append((startx - 2, starty - 1))
                    if (tmp_mapper[startx - 2][starty - 1] != 1):
                        tmp[startx - 2][starty - 1] = 1
                        mapper_queue.append((tmp, startx - 2, starty - 1, tmp_prev_path))
                    if canwritelog(tmp):
                        writelog(tmp, tmp_prev_path)  # !!!
                if (startx - 2 >= 0) and (starty + 1 < 3):
                    tmp = deepcopy(tmp_mapper)
                    tmp_prev_path = deepcopy(prev_path)
                    tmp_prev_path.append((startx - 2, starty + 1))
                    if (tmp_mapper[startx - 2][starty + 1] != 1):
                        tmp[startx - 2][starty + 1] = 1
                        mapper_queue.append((tmp, startx - 2, starty + 1, tmp_prev_path))
                    if canwritelog(tmp):
                        writelog(tmp, tmp_prev_path)  # !!!
                # print "round "+str(rounds)
                rounds += 1

    print "finished..."


def cur_file_dir():
    # 获取脚本路径
    path = sys.path[0]
    # 判断为脚本文件还是py2exe编译后的文件，如果是脚本文件，则返回的是脚本的目录，
    # 如果是py2exe编译后的文件，则返回的是编译后的文件路径
    if os.path.isdir(path):
        return path
    elif os.path.isfile(path):
        return os.path.dirname(path)


def printkeytable():
    print "[*]Fallow the map below to enter the device:"
    print "[*]===================="
    print "[*]=00 01 02  |  o o o="
    print "[*]=10 11 12  |  o o o="
    print "[*]=20 21 22  |  o o o="
    print "[*]===================="


def decrypthash():
    print "[*]Hash database detected."
    # print cur_file_dir() + '\\' + sys.argv[1]
    if (len(sys.argv) < 2):
        print "[*]Please run the script file with key file name ."
    else:
        if os.path.isfile(cur_file_dir() + '\\' + sys.argv[1]):
            print "[*]Get key information now......"
            keyhandle = open(cur_file_dir() + '\\' + sys.argv[1], 'rb')
            gesturebytes = keyhandle.read()
            gesturetext = binascii.b2a_hex(gesturebytes)
            print "[*]Crypted hash is :\n  " + gesturetext
            print "[*]Decoding now....................."
            keyhandle.close()
            filehandle = open(db, 'r')
            for line in filehandle:
                if not line.find(gesturetext) == -1:
                    print "[*]Sucess cracked the gesture:"
                    print line
                    printkeytable()
                    print "============================================="
            filehandle.close()


if __name__ == '__main__':

    print "============================================="
    print "[*]Android lockscreen(gesture) cracker"
    print "[*]Updated by obaby QQ:289090351"
    print "[*]Mars Information Security"
    print "[*]http://www.h4ck.org.cn"
    print "[*]Thx tog0t3n for his/her orginal script"
    print "============================================="
    print "[*]Detect if hash database is exists....."

    if os.path.isfile(db) == False:
        filehandle = open(db, 'w')
        generatehashtable()
        decrypthash()
    else:
        decrypthash()
