# coding:utf-8
import os
import chnSegment
import plotWordcloud
import connect_database
import sys
import re

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

try:
    #generate(1029108019, "Arcaea重金属超标群")
    generate(int(sys.argv[1]), sys.argv[2])
    if(os.path.isfile(sys.path[0] + "/Images/" + sys.argv[1] + ".jpg") == True):
        print(sys.path[0] + "/Images/" + sys.argv[1] + ".jpg")
    else:
        print("OSError: [Errno 2] No such file or directory")

except Exception as sb:
    print(repr(sb))