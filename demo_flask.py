# coding:utf-8
import os
import chnSegment
import plotWordcloud
import connect_database
import sys
import re
from rwini import *
import time
from pymysql import OperationalError
import settings

def generate(groupnum:int, groupname:str):

    stat = connect_database.get_text(groupnum)
    
    if(stat[0] == False):
        print(stat[1])
        sys.exit()
    else:
        text_g = stat[1]
        text = ""
        for t in text_g:
            text_p = t['Message']

            sysmsg = re.findall("\[.*\]", text_p)
            if(len(sysmsg) > 0):
                for sy in sysmsg:
                    text_p = text_p.replace(sy, "")

            #try:
             #   text_p = text_p.encode("utf-8")
            #except:
             #   print("fail", text_p)
              #  continue
            if("<?xml version=" not in text_p):
                text = text + " " + text_p

        text = chnSegment.word_segment(text)#中文分词

    plotWordcloud.generate_wordcloud(text, str(groupnum), groupname)

#generate(1029108019, "Arcaea重金属超标群")

def out(groupnum:int, groupname:str):
    try:
        #generate(1029108019, "Arcaea重金属超标群")
        generate(groupnum, groupname)

        写配置项("stat.ini", "wcstat", str(groupnum), '0') #0-处理完成

        if(os.path.isfile(sys.path[0] + "/Images/" + str(groupnum) + ".jpg") == True):
            print("处理完成")
            写配置项("stat.ini", "wctime", str(groupnum), str(int(time.time())))
        else:
            print("Oserr")
            写配置项("stat.ini", "wcstat", str(groupnum), "OSError: [Errno 2] No such file or directory") #非0/1，输出错误信息

    except Exception as sb:
        写配置项("stat.ini", "wctime", str(groupnum), str(int(time.time()) - settings.cold + 60))
        写配置项("stat.ini", "wcstat", str(groupnum), repr(sb)) #非0/1，输出错误信息
        print("完成:")
        print(repr(sb))