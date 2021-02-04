# !/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File       : fakerData.py
@Time       : 2021/2/3 17:49
@Author     : Hugh
@version    : TODO
@Description: TODO

"""


from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "sqlite:///./app/app.db"

engine = create_engine(SQLALCHEMY_DATABASE_URL,connect_args={"check_same_thread": False})

SessionLocal =sessionmaker(autocommit=False,autoflush=False,bind=engine)

Base = declarative_base()
