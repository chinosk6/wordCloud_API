from flask import Flask, send_file, request, jsonify
import settings
from threading import Thread
import demo_flask as wcrun
from rwini import *
import time
import os
import base64
import io

ip = settings.ip
port = settings.port

app = Flask(__name__)

def async_qwq(f):
    def task_qwq(*args, **kwargs):
        t = Thread(target=f, args=args, kwargs=kwargs)
        t.start()
    return(task_qwq)

@async_qwq
def gene(groupid, groupname):
    gstat = 读配置项("stat.ini", "wcstat", str(groupid), 空项返回 = '0')
    if(gstat != '1'): #不在处理队列,开始处理
        写配置项("stat.ini", "wcstat", str(groupid), '1') #1-处理中 0-未处理或护理完成
        wcrun.out(int(groupid), groupname)
    else: #已在处理队列
        pass

@app.route('/wordcloud', methods=["GET"])
def req():
    groupid = request.args.get("id")
    groupname = request.args.get("name")

    ts = int(读配置项("stat.ini", "wctime", groupid, 空项返回 = '0'))
    time_now = int(time.time()) #10位时间戳(s)

    if(ts + settings.cold > time_now): #冷却
        if(os.path.isfile("./Images/" + groupid + ".jpg") == True):

            return(jsonify({'stat': 200, 'msg': '下次缓存刷新时间:' + str(ts + settings.cold - time_now) + '秒', 'file': settings.host + '/getwcimg?id=' + groupid}), 200)
        else:
            return(jsonify({'stat': 500, 'msg': 读配置项("stat.ini", "wcstat", groupid, "未知错误") + ' ' + '下次缓存刷新时间:' + str(ts + settings.cold - time_now) + '秒', 'file': ''}), 500)

    else:
        gene(groupid, groupname)
        return(jsonify({'stat': 202, 'msg': 'building', 'file': ''}), 202)

    return(groupid + groupname)

@app.route('/getwcimg')
def qwq():
    groupid = request.args.get("id")

    with open("./Images/" + groupid + ".jpg", 'rb') as bites:
        return send_file(
            io.BytesIO(bites.read()),
            mimetype='image/jpg'
        )

if __name__ == '__main__':                        #正式部署请使用下面的代码
    app.run(ip, port ,debug=True) 
#if __name__ == "__main__":
#    from waitress import serve
#    serve(app, host=ip,port=port)