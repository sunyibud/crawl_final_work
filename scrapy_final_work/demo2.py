# -*- coding: utf-8 -*-
# @Time    : 2021/12/3 0:44
# @Author  : HPTOUS
# @FileName: demo2.py
# @describe:
# @Software: PyCharm
# import requests
# headers = {
#             "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:93.0) Gecko/20100101 Firefox/93.0"
#         }
# url = r'https://api.github.com/_private/browser/stats'
# resp = requests.post(url=url, headers=headers)
# print(resp.text)
# resp.close()
import copy
import re

# lst = lis = ["2", "8", "6", "5", "0"," 9", "4", "7", " 7", '6',' 8', '5', '8', '2', '1',' 6']
# a, b = 2, 4
# with open("./1.txt", "a", encoding='utf-8') as fp:
#     fp.write(str(a) + str(b))
'''
1、Jan. January 一月；
2、Feb. February 二月；
3、Mar. March 三月；
4、Apr. April 四月；
5、May无缩写 五月；
6、Jun. June 六月；
7、Jul. July 七月；
8、Aug. August 八月；
9、Sep. September九月；
10、Oct. October 十月；
11、Nov. November 十一月；
12、Dec. December 十二月
'''


def monthjuedgement():
    month = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    a = ['Nov 4, 2020', 'Dec 26, 2020', 'Nov 3, 2020', 'Nov 3, 2020', 'Nov 24, 2020', 'Jan 2, 2020', 'Dec 19, 2020',
         'Dec 13, 2020', 'Dec 6, 2020', 'Dec 24, 2020', 'Dec 24, 2020', 'Sep 3, 2021', 'Dec 3, 2020']
    a = [re.split(r"\s+", re.sub(r"[,\s+]", " ", a[i])) for i in range(len(a))]
    # print(a)
    a = sorted(a, key=lambda x: x[2], reverse=True)
    print("1", a)
    year = a[0][2]
    for time1 in a:
        if not time1[2] == year:
            c = a.index(time1)
            print("c", c)
            a = a[:c]
            break

    print("2", a)
    for i in range(len(a)):
        a[i][0] = month.index(a[i][0])
    a = sorted(a, key=lambda x: x[0], reverse=True)
    print("3", a)
    e = 0
    for time2 in a:
        print(time2[0], a[0][0])
        if not time2[0] == a[0][0]:
            e = a.index(time2)
            print("e", e)
            a = a[:e]
            break

    print("4", a)
    a = sorted(a, key=lambda x: x[1], reverse=True)
    for i in range(len(a)):
        a[i][0] = month[a[i][0]]
    print("5", a)
    print(a[0][0] + " " + a[0][1] + ", " + a[0][2])


lst = []
print(lst is list())
