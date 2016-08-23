# -*- coding:utf-8 -*-
from sqlalchemy import Column,String,create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# 创建对象基类
Base = declarative_base()

# 定义user对象
class City(Base):
    # 表的名字
    __tablename__ = 'city'

    # 表的结构
    id = Column(String(11), primary_key=True)
    addr_code = Column(String(50))
    location = Column(String(50))
    pid = Column(String(10))

# 初始化数据库连接
engine = create_engine('mysql+mysqlconnector://root:admin@10.134.9.49:3306/test')
# 创建DBSession类型
DBSession = sessionmaker(bind=engine)

# 创建session对象
session = DBSession()
# 创建city对象
new_city = City('')
