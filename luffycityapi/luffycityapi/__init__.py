import pymysql

pymysql.version_info = (1, 4, 6, "final", 0)  # 伪装版本号欺骗 Django 检查
pymysql.install_as_MySQLdb()