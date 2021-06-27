# wordCloud_API
词云API版,用于统计群友说过的怪话,基于[wordCloud][1]

消息储存在mysql数据库中.数据表结构见`table.sql`

为啥要做成API:这玩意太吃性能了,如果和Bot放在同一个服务器,可能会影响到bot的正常运行

~~你服务器性能够用的话就当我在放屁~~

## 依赖包
```python
pip install jieba
pip install wordcloud
pip install flask
pip install pymysql
```

- `wordcloud`依赖:`Pillow`，`numpy`，`matplotlib`

## 部署
- 先记录信息到数据库中

- 在`settings.py`中填写对应信息

## 启动服务

- Windows

```sh
python apprun.py
```

- Linux : 

```shell
调试: python apprun.py
运行: nohup python -u apprun.py > wc.log 2>&1 &
```

## 调用方式

由于直接返回图片可能会超时,故采用**轮询**的方式调用

- 访问`http://example.com/wordcloud?id=群号&name=群名`

##### 你可能会得到以下结果中的一个:

###### 图片生成中:

此时你应该继续访问相同的地址,直到`stat`参数值为`200`或`500`时停止

```json
{
    "file": "",
    "msg": "building",
    "stat": 202
}
```

###### 调用成功:

访问`file`内的网址,不出意外的话,你将可以得到一张生成完毕的图片

```json
{
    "file": "http://example.com/getwcimg?id=549090812",
    "msg": "下次缓存刷新时间:28659秒",
    "stat": 200
}
```

###### 调用失败:

`msg`将会提示发生错误的原因

```json
{
    "file": "",
    "msg": "ProgrammingError(1146, \"Table 'qqmsglog.999' doesn't exist\") 下次缓存刷新时间:58秒",
    "stat": 500
}
```

## 直接调用

你也可以选择不使用API,直接调用

```sh
python demo.py 群号 群名
```

完成后将返回图片路径

## 生成结果例:



[1]: https://github.com/fuqiuai/wordCloud
