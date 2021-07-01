ip = '127.0.0.1'
port = 11451
cold = 8*3600 #冷却时间(秒)
jcold = 360 #json请求冷却时间
host = 'http://example.com' #填写你的api地址。例子：调用地址为 http://example.com/wordcloud?id=群号&name=群名 时,此处填写 http://example.com
ignore_id = [514, 114] #此处填写需要无视的QQ号
max_words = 900 #最大词数
keys = ["141", "fdwed"]

class mysql:
    host = ''
    port = 3306
    db = ''
    user = ''
    password = ''
