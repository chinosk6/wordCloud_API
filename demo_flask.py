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

def generate(groupnum:int, groupname:str, bg, bgtext, pkey):

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
            if(("<?xml version=" not in text_p) and (t['QQ'] not in settings.ignore_id)):
                text = text + " " + text_p

        text = chnSegment.word_segment(text)#中文分词

    plotWordcloud.generate_wordcloud(text, str(groupnum), groupname, bg, bgtext, pkey)
    return(len(text_g))

#generate(1029108019, "Arcaea重金属超标群")

def out(groupnum:int, groupname:str, bg:str, bgtext:str, pkey:str):
    try:
        #generate(1029108019, "Arcaea重金属超标群")
        num = generate(groupnum, groupname, bg, bgtext, pkey)

        写配置项("stat.ini", "wcstat", str(groupnum) + pkey, '0') #0-处理完成

        if(os.path.isfile(sys.path[0] + "/Images/" + str(groupnum) + pkey + ".jpg") == True):
            print("处理完成")
            写配置项("stat.ini", "wctime", str(groupnum) + pkey, str(int(time.time())))
            写配置项("stat.ini", "wcstat", str(groupnum) + pkey, "共处理:" + str(num) + "条消息。")
        else:
            print("Oserr")
            写配置项("stat.ini", "wcstat", str(groupnum) + pkey, "OSError: [Errno 2] No such file or directory") #非0/1，输出错误信息

    except Exception as sb:
        写配置项("stat.ini", "wctime", str(groupnum) + pkey, str(int(time.time()) - settings.cold + 60))
        写配置项("stat.ini", "wcstat", str(groupnum) + pkey, repr(sb)) #非0/1，输出错误信息
        print("完成:")
        print(repr(sb))



def jsonout(bg:str, jsonlist:list, pkey:str):
    try:
        
        plotWordcloud.generate_jsoncloud(jsonlist, bg, pkey)
        写配置项("stat.ini", "wcstat", pkey, '0') #0-处理完成

        if(os.path.isfile(sys.path[0] + "/Images/" + pkey + ".png") == True):
            print("处理完成")
            写配置项("stat.ini", "wctime", pkey, str(int(time.time())))
        else:
            print("OSerr")
            写配置项("stat.ini", "wcstat", pkey, "OSError: [Errno 2] No such file or directory") #非0/1，输出错误信息

    except Exception as sb:
        写配置项("stat.ini", "wctime", pkey, str(int(time.time()) - settings.jcold + 60))
        写配置项("stat.ini", "wcstat", pkey, repr(sb)) #非0/1，输出错误信息
        print("完成:")
        print(repr(sb))