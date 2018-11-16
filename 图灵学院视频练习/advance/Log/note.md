# LOG
## logging模块
- 日志的级别
    - DEBUG
    - INFO
    - NOTICE
    - WARNING
    - ERROR
    - CRITICAL
    - ALERT
    - EMERGENCY
- 函数
    - logging.debug(msg, *args, **kwargs) 创建一条严重级别为DEBUG的日志记录
    - logging.info(msg, *args, **kwargs) 创建一条严重级别为INFO的日志记录
    - logging.warning(msg, *args, **kwargs) 创建一条严重级别为WARNING的日志记录
    - logging.error(msg, *args, **kwargs) 创建一条严重级别为ERROR的日志记录
    - logging.critical(msg, *args, **kwargs) 创建一条严重级别为CRITICAL的日志记录
    - logging.log(level, *args, **kwargs) 创建一条严重级别为level的日志记录
    - logging.basicConfig(**kwargs) 对root logger进行一次性配置
        - 只在第一次调用的时候起作用
        - 不配置logger则使用默认值
            - 输出: sys.stderr
            - 级别: WARNING
            - 格式: level:log_name:content

- format参数
 
# logging模块的处理流程
- 四大组件

    - 日志器(Logger): 产生日志的一个接口
    - 处理器(Handler):把产生的日志发送到相应的目的地
    - 过滤器(Filter): 更精细的控制那些日志输出
    - 格式器(Formatter): 对输出信息进行格式化
- 操作
    -  Logger.setLevel() 	设置日志器将会处理的日志消息的最低严重级别
    -  Logger.addHandler() 和 Logger.removeHandler() 	为该logger对象添加 和 移除一个handler对象
    -  Logger.addFilter() 和 Logger.removeFilter() 	为该logger对象添加 和 移除一个filter对象
    -  Logger.debug: 产生一条debug级别的日志，同理，info，error，等
    -  Logger.exception(): 创建类似于Logger.error的日志消息
    -  Logger.log():获取一个明确的日志level参数类创建一个日志记录
    
- 
    
    
    
    
    
    
    
    
    
    
    
    