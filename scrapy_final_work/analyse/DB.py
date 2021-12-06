# -*- coding: UTF-8 -*-
# @Time : 2021/05/15
# @Author : Sunyi
# @File : pymysql_demo.py
# @Detail : 数据库操作(增，删， 改， 查）
import pymysql


class DB:
    def __init__(self, user, password, db):
        self.__conn = pymysql.connect(host='120.27.245.194', user=user, password=password, port=3306, db=db)
        if self.__conn is not None:
            print("成功连接数据库：" + db)
        else:
            print("数据库连接失败")

    def create_table(self, table, structure, primary_key):  # 新建表
        cur = self.__conn.cursor()
        sql = 'create table if not exists ' \
              + table + '(' + structure + 'primary key(' + primary_key + '))'
        # print(sql)
        cur.execute(sql)
        cur.close()
        print("成功创建表：" + table)

    def insert(self, table, data):
        cur = self.__conn.cursor()  # 生成游标
        sql = 'insert into ' + table + ' values(' + data + ')'
        try:
            cur.execute(sql)
            self.__conn.commit()
            # print('受影响行数：', cur.rowcount)
        except Exception as e:
            print(e)
            self.__conn.rollback()
        finally:
            cur.close()  # 关闭游标
        # print("成功向表" + table + "插入一条数据")

    def search(self, sql):
        cur = self.__conn.cursor()
        cur.execute(sql)
        res = cur.fetchall()  # 通过fetchall方法获得数据
        return res

    def operate(self, sql):
        cur = self.__conn.cursor()
        try:
            cur.execute(sql)
            self.__conn.commit()
            # print('受影响行数：', cur.rowcount)
        except Exception as e:
            print(e)
            self.__conn.rollback()
        finally:
            cur.close()  # 关闭游标
        print(sql + "操作成功")

    def close(self):
        self.__conn.close()
