SECRET_KEY = 'hadnsjdbqmslmdasofs'

# 数据库的配置信息
HOSTNAME = '127.0.0.1'
POST = 3306
USERNAME = 'root'
PASSWORD = '123456'
DATABASE = 'resume'
SQLALCHEMY_DATABASE_URI = f'mysql+pymysql://{USERNAME}:{PASSWORD}@{HOSTNAME}:{POST}/{DATABASE}?charset=utf8mb4'