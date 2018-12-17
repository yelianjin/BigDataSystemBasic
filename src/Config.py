#!/usr/bin/python
# -*- coding:utf-8 -*-


# 基类，调试作用
class Config(object):
    DEBUG = False


# 不同节点配置，派生基类
class DealerConfig(Config):
    LISTEN_SOCKET = ("0.0.0.0", 23456)

