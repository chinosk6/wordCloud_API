from configobj import ConfigObj  


def 读配置项(文件名, 节, 项, 空项返回: str = ''):
    config = ConfigObj(文件名, encoding='UTF8')  
    try:
        res = config[节][项]
    except:
        res = 空项返回

    return(res)

def 写配置项(文件名, 节, 项, 值):
    config = ConfigObj(文件名, encoding='UTF8')
    if(节 not in config):
        config[节] = {}

    config[节][项] = 值
 
    config.write()