# coding=utf-8
import sqlite3
import time
from uuid import uuid1
import os


def uuid():
    return uuid1()

#用参数拼接sql语句，然后送到数据库执行，再返回结果
class Sql():#数据库操作，常用操作封装，包括，insert、delete、update、select
    def __init__(self):
        self.__conn = sqlite3.connect('CheckWork.db')
        self.__cursor = self.__conn.cursor()

    def __del__(self):
        self.__conn.close()

    def commit(self):
        self.__conn.commit()

    def execute(self, sql):
        self.__cursor.execute(sql)

    def insert(self, tab, dss):
        try:
            for ds in dss:
                keyCon = len(ds)
                esql = "INSERT INTO "+ tab +" VALUES("
                con = 1
                for d in ds:
                    if type(d) == type(0):
                        esql += str(d) + ('' if con == keyCon else ',')
                    else:
                        esql += "'" + d + "'" + ('' if con == keyCon else ',')
                    con += 1
                esql += ');'
                # print(esql)
                self.execute(esql)
            self.commit()
        except:
            return False
        return True

    def delete(self, tab, whe=None):
        try:
            sql = "delete from " + tab + self.whe(whe)
            # print(sql)
            self.execute(sql)
            self.commit()
        except:
            return False
        return True

    def update(self, tab, setss, whe=None):
        try:
            sql = "update " + tab + " set " + self.getSet(setss) + self.whe(whe)
            # print(sql)
            self.execute(sql)
            self.commit()
        except:
            return False
        return True

    def get(self, tab, col='*', whe=None):
        try:
            sql = "select " + self.col(col) + " from " + tab + self.whe(whe)
            # print(sql)
            self.execute(sql)
            return self.__cursor.fetchone()
        except:
            return None

    def select(self, tab, col='*', whe=None, order=''):
        try:
            sql = "select " + self.col(col) + " from " + tab + self.whe(whe)+order
            # print(sql)
            self.execute(sql)
            return self.__cursor.fetchall()
        except:
            return []

    def col(self,col):
        if col == "*":
            return '*'
        res = ''
        try:
            keyCon = len(col)
            con = 1
            for c in col:
                res += c + ('' if con == keyCon else ',')
                con += 1
            return res
        except:
            return '*'

    def whe(self, whe):
        res = ''
        if whe is None:
            return res
        try:
            keyCon = len(whe)
            con = 1
            for key in whe:
                if isinstance(whe[key], str):
                    res += key + "='" + whe[key] + "'" + ('' if con == keyCon else ' and ')
                else:
                    res += key + "=" + str(whe[key]) + ('' if con == keyCon else ' and ')
                con += 1
        except:
            return ''
        return " where " + res if whe is not None else ''

    def getSet(self,sets):
        keyCon = len(sets)
        con = 1
        req = ''
        for key in sets:
            if isinstance(sets[key], str):
                req += key + "='" + sets[key] + "'" + ('' if con == keyCon else ',')
            else:
                req += key + "=" + str(sets[key]) + ('' if con == keyCon else ',')
            con += 1
        return req
