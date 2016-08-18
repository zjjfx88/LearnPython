# -*- coding:utf-8 -*-
from sqlalchemy import Column,String,create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# 创建对象基类
Base = declarative_base()

# 定义user对象
class User(Base):
    # 表的名字
    __tablename__ = 'city'

    # 表的结构
    id = Column(String(11), primary_key=True)
    addr_code = Column(String(50))
    location = Column(String(50))
