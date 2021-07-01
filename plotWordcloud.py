# coding:utf-8

from os import path
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS
import time
import settings

def draw_text(wc, groupnum:str, groupname:str, bgtext, pkey):
    from PIL import ImageDraw, ImageFont
    pt = wc.to_image()
    #pt = Image.new('RGB', (1200,1200), 0)
    draw = ImageDraw.Draw(pt)
    font = ImageFont.truetype(font='./font/msyh.ttf',size = int(39*1.5))

    t_w,t_h = font.getsize(groupname)    #宽度判断
    if(t_w > 405*1.5):
        while(t_w > 360*1.5):
            groupname = groupname[:-1]
            t_w,t_h = font.getsize(groupname)
        groupname = groupname + '...'

    draw.text(xy=(int(18*1.5), int(971*1.5)),text = groupname, fill=(67, 63, 151),font=font)

    font = ImageFont.truetype(font='./font/msyh.ttf',size = int(33*1.5))
    draw.text(xy=(int(18*1.5), int(1025*1.5)),text = groupnum, fill=(35, 143, 88),font=font)

    time_now = time.strftime("%Y-%m-%d %H:%M", time.localtime(time.time()))
    font = ImageFont.truetype(font='./font/msyh.ttf',size = int(37*1.5))
    draw.text(xy=(int(18*1.5), int(1068*1.5)),text = time_now, fill=(119, 41, 124),font=font)

    font = ImageFont.truetype(font='./font/msyh.ttf',size = int(21*1.5))
    draw.text(xy=(int(18*1.5), int(1154*1.5)),text = bgtext, fill=(202, 80, 163),font=font)

    pt.save('./Images/' + groupnum + pkey + '.jpg', quality = 100)

def generate_wordcloud(text, groupnum:str, groupname:str, bg, bgtext, pkey):

    d=path.dirname(__file__)
    alice_mask = np.array(Image.open(path.join(d, "Images/" + bg + ".png"))) #背景图
    font_path=path.join(d,"font//msyh.ttf")
    st = [] #set(STOPWORDS)

    with open("./doc/cn_stopwords.txt", "r", encoding='utf-8') as stops:
        for stop in stops:
            st.append(stop.replace("\n", ""))

    wc = WordCloud(background_color="white",# 设置背景颜色
           max_words = settings.max_words, # 词云显示的最大词数  
           mask = alice_mask,# 设置背景图片       
           stopwords = st, # 设置停用词
           font_path = font_path, # 兼容中文字体，不然中文会显示乱码
                  )
    # 生成词云 
    wc.generate(text)
    draw_text(wc, groupnum, groupname, bgtext, pkey)
    # 生成的词云图像保存到本地
    #wc.to_file(path.join(d, "Images//alice.png"))
    

    # 显示图像
    #plt.imshow(wc, interpolation='bilinear')
    # interpolation='bilinear' 表示插值方法为双线性插值
    #plt.axis("off")# 关掉图像的坐标
    #plt.show()

def listtotext(jsonlist:list):
    vsum = 0
    alltext = ""
    for nb in jsonlist:
        vsum = vsum + nb['value'] #求value和

    for sb in jsonlist:
        prop = int(sb['value'] / vsum * 1000)
        alltext = alltext + ' ' + (sb['_id'] + '  ') * prop
    return(alltext)

def generate_jsoncloud(jsonlist:list, bg, pkey):
    text = listtotext(jsonlist)

    d=path.dirname(__file__)
    alice_mask = np.array(Image.open(path.join(d, "Images/" + bg + ".png"))) #背景图
    font_path=path.join(d,"font//msyh.ttf")
    st = [] #set(STOPWORDS)

    with open("./doc/cn_stopwords.txt", "r", encoding='utf-8') as stops:
        for stop in stops:
            st.append(stop.replace("\n", ""))

    wc = WordCloud(background_color="white",# 设置背景颜色
           max_words = settings.max_words, # 词云显示的最大词数  
           mask = alice_mask,# 设置背景图片       
           stopwords = st, # 设置停用词
           font_path = font_path, # 兼容中文字体，不然中文会显示乱码
           collocations = False
                  )
    # 生成词云 
    #print(text)
    wc.generate(text)
    wc.to_file(path.join(d, "Images/" + pkey + ".png"))
    #draw_text(wc, groupnum, groupname, bgtext, pkey)