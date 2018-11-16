import logging

Log_Format = "%(asctime)s======%(levelname)s+++++++%(message)s"

# 按照自己的意愿, 对root logger进行一次配置(个性化的配置)
# 默认level=WARNING 当级别低于WARNING的logging不会输出
logging.basicConfig(filename="tulingxueyuan.log", level=logging.DEBUG, format=Log_Format)

logging.debug("This is a debug log.")
logging.info("This is a info log.")
logging.warning("This is a warning log.")
logging.error("This is a error log.")
logging.critical("This is a critical log.")

logging.log(logging.DEBUG,"This is a debug log.")
logging.log(logging.INFO, "This is a info log.")
logging.log(logging.WARNING, "This is a warning log.")
logging.log(logging.ERROR, "This is a error log.")
logging.log(logging.CRITICAL, "This is a critical log.")