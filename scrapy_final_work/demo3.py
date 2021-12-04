# -*- coding: utf-8 -*-
# @Time    : 2021/12/3 15:48
# @Author  : HPTOUS
# @FileName: demo3.py
# @describe:
# @Software: PyCharm
import re

# a = [[10, '3', '2021'], [8, '3', '2021'], [0, '3', '2021'], [0, '3', '2021'], [0, '2', '2021']]
# a = a[:2]
# print(a)
# s = 'Nov 30, 2021'
# s = re.split(r"[,\s]", s)
# s.remove("")
# s = " ".join(s)
# print(s)
# s = None
# if s == "" or s is None or len(s):
#     print("jinru")
import pymysql

connect = pymysql.Connect(
    host='120.27.245.194',
    port=3306,
    user='root',
    password='Zx4653397..',
    database='github',
    charset='utf8')
cursor = connect.cursor()

# item = {
#     "Topic_name": "3D",
#     "topic_number": "4776",
#     "topic_describe": "3D modeling is the process of virtually developing the surface and structure of a 3D object.",
# }
item = {
    "project_belong_topic": "3D",
    "project_name": "justjavac",
    "project_owner": "free-programming-books-zh_CN",
    "project_path": "https://github.com/justjavac/free-programming-books-zh_CN",
    "project_star": "84.7k",
    "project_fork": "24.3k",
    "project_revise_time": "Jan 8 2021",
    "project_commit_number": "911",
    "project_label": "/react//javascript//android//kotlin//python//swift//pdf//ios//angular//react-native//programming//books//vue//free//",
    "project_languages": "JavaScript72.2%CSS19.5%Less6.8%HTML1.5%",
    "project_describe": "免费的计算机编程类中文书籍 欢迎投稿",
    "project_download_zip": "https://github.com/marktext/marktext/archive/refs/heads/develop.zip",
    "project_clone_ssh": "@//github.com/tesseract-ocr/tessdata.git",

}
try:
    # cursor.execute('insert into Topics values(NULL, "%s", "%s", "%s")' % (item["Topic_name"], item["topic_number"], item["topic_describe"]))
    # cursor.execute('insert into Projects values(NULL,"%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s")'
    #     % (item["project_belong_topic"], item["project_name"], item["project_owner"], item["project_path"],
    #        item["project_star"],
    #        item["project_fork"], item["project_revise_time"], item["project_commit_number"],
    #        item["project_label"], item["project_languages"], item["project_describe"],
    #        item["project_download_zip"], item["project_clone_ssh"]))
    lst = [13004, 13005, 13006, 13007, 13008, 13009]
    cursor.executemany('delete from HTTP where id=%s', lst)
    connect.commit()
    print("success")
except Exception as e:
    print(e)
    connect.rollback()
print("1")
