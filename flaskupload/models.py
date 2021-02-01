#!/usr/bin/python
# -*- coding: utf-8 -*-
from app_config import app
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy(app)
# 创建数据库模型
class Info(db.Model):
    __tablename__ = 'house_info'
    h_no = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(2000), nullable=True)
    type = db.Column(db.String(2000), nullable=True)
    area = db.Column(db.Float, nullable=True)
    face = db.Column(db.String(2000), nullable=True)
    floor = db.Column(db.String(2000), nullable=True)
    addr_dist = db.Column(db.String(2000), nullable=True)
    addr_name = db.Column(db.String(2000), nullable=True)
    price = db.Column(db.Float, nullable=True)

    def __repr__(self):
        return '<Info %r>' % self.job