ip = '127.0.0.1'
port = 11451
cold = 8*3600 #冷却时间(秒)
host = 'http://example.com' #填写你的api地址。例子：调用地址为 http://example.com/wordcloud?id=群号&name=群名 时,此处填写 http://example.com
ignore_id = [114514, 1919810] #此处填写需要无视的QQ号

class mysql:
    host = ''
    port = 3306
    db = 'qqmsglog'
    user = ''
    password = ''

