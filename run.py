# !/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File       : run.py
@Time       : 2021/2/4 8:56
@Author     : Hugh
@version    : TODO
@Description: TODO

"""

import uvicorn
from app.main import app

if __name__ == '__main__':
    uvicorn.run("app.main:app",reload=True)