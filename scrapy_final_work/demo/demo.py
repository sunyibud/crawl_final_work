# -*- coding: utf-8 -*-
# @Time    : 2021/12/1 21:58
# @Author  : HPTOUS
# @FileName: demo.py
# @describe:
# @Software: PyCharm
import re

# s = """Here are
#             4,766,123 public repositories
#             matching this topic..."""
#
# lst = ['\n          ', '\n            mrdoob\n', '          /\n          ', '\n            three.js\n', '        ']
#
# lst = [lst[i].strip().replace(" ", "") for i in range(len(lst))]
# print("".join(lst).strip())
#
# # obj = re.compile("\d+")
# # number = "".join(obj.findall(s))
# # print(number)
# s = "mrdoob/three.js"
# lst = s.split("/")
# print(lst)

import requests
from urllib3.exceptions import InsecureRequestWarning
from lxml import etree

url = r'https://github.com/swlib/saber'
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:93.0) Gecko/20100101 Firefox/93.0"
}
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
resp = requests.get(url=url, headers=headers, verify=False)
with open('githubdemo.html', 'w', encoding='utf-8') as f:
    f.write(resp.text)
tree = etree.HTML(resp.text)
resp.close()
# f = open('./githubdemo.html', 'rb')
# content = f.read().decode('utf-8')
# tree = etree.HTML(content)
project_li_line = tree.xpath('//*[@id="repository-container-header"]/div[1]/ul/li')
project_star, project_fork = 0, 0
for li in project_li_line:
    temp = li.xpath('.//text()')
    temp = "".join([temp[i].strip() for i in range(len(temp))])
    print("temp:", temp)
    if "Star" in temp:
        project_star = "".join(re.findall(r"[.\d+]", temp))
        if temp[-1] == "k":
            project_star += "k"
        continue
    if "Fork" in temp:
        project_fork = "".join(re.findall(r"[.\d+]", temp))
        if temp[-1] == "k":
            project_fork += "k"
        continue
print("project_star", project_star)
print("project_fork", project_fork)


def Judgement_Date(file_revise_time):
    month = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    file_revise_time = [re.split(r"\s+", re.sub(r"[,\s+]", " ", file_revise_time[i])) for i in
                        range(len(file_revise_time))]
    file_revise_time = sorted(file_revise_time, key=lambda x: x[2], reverse=True)
    print("1", file_revise_time)
    for revise_time in file_revise_time:
        if not revise_time[2] == file_revise_time[0][2]:
            dif_year = file_revise_time.index(revise_time)
            file_revise_time = file_revise_time[:dif_year]
            break
    print("2", file_revise_time)
    for i in range(len(file_revise_time)):
        file_revise_time[i][0] = month.index(file_revise_time[i][0])
    file_revise_time = sorted(file_revise_time, key=lambda x: x[0], reverse=True)
    print("3", file_revise_time)
    for revise_time in file_revise_time:
        if not revise_time[0] == file_revise_time[0][0]:
            dif_month = file_revise_time.index(revise_time)
            file_revise_time = file_revise_time[:dif_month]
            break

    print("4", file_revise_time)
    file_revise_time = sorted(file_revise_time, key=lambda x: x[1], reverse=True)
    for i in range(len(file_revise_time)):
        file_revise_time[i][0] = month[file_revise_time[i][0]]
    print("5", file_revise_time)
    # nealy_time = file_revise_time[0][0] + " " + file_revise_time[0][1] + ", " + file_revise_time[0][2]
    if file_revise_time == "" or file_revise_time is None or len(file_revise_time) == 0:
        return "Null"
    else:
        nealy_time = " ".join(file_revise_time[0])
        if nealy_time == "" or nealy_time is None:
            nealy_time = "Null"
        return nealy_time


# project_watch = tree.xpath('//*[@id="repository-container-header"]/div[1]/ul/li[2]/notifications-list-subscription-form/a/text()')
# print("project_watch:", project_watch)#//*[@id="repository-container-header"]/div[1]/ul/li[2]/div/a[2]
# project_star = tree.xpath('//*[@id="repository-container-header"]/div[1]/ul/li[4]/a[2]/text()')[0].strip()
# print("project_star", project_star)#//*[@id="repository-container-header"]/div[1]/ul/li[4]/a[2]
# project_fork = tree.xpath('//*[@id="repository-container-header"]/div[1]/ul/li[3]/div/a[2]/text()')[0].strip()
# print("project_fork", project_fork)
#                                 //*[@id="repo-content-pjax-container"]/div/div[2]/div[1]/div[2]/div[1]/div/div[2]/div[2]/a[3]/relative-time
#                                 //*[@id="repo-content-pjax-container"]/div/div[2]/div[1]/div[2]/div[1]/div/div[2]/div[2]/a[2]/relative-time
project_revise_time = tree.xpath(
    '//*[@id="repo-content-pjax-container"]/div/div[2]/div[1]/div[2]/div[1]/div/div[2]/div[2]//relative-time/text()')
print("project_revise_time", project_revise_time)
if len(project_revise_time) == 0 or project_revise_time is [] or project_revise_time is None or project_revise_time == "":
    project_final_revise_time_list = tree.xpath(
        '//*[@id="repo-content-pjax-container"]/div/div[2]/div[1]/div[2]/div[3]/div[1]/div[@role="row"]//time-ago/text()')
    print("project_final_revise_time_list", project_final_revise_time_list)
    project_revise_time = Judgement_Date(project_final_revise_time_list)
else:
    print("进入了else")
    project_revise_time = re.split(r"[,\s+]", project_revise_time[0])
    project_revise_time.remove("")
    project_revise_time = " ".join(project_revise_time)
print("project_revise_time", project_revise_time)
#  //*[@id="repo-content-pjax-container"]/div/div[2]/div[1]/div[2]/div[3]/div[1]
# for revise_time in project_final_revise_time_list:
#     print("revise_time", revise_time)
#     change_time = revise_time.xpath('.//time-ago/text()')
#     print("change_time", change_time)
# //*[@id="repo-content-pjax-container"]/div/div[2]/div[1]/div[2]/div[1]/div/div/ul/li/a/span/strong
project_commit_number = tree.xpath(
    '//*[@id="repo-content-pjax-container"]/div/div[2]/div[1]/div[2]/div[1]/div/div[@class="flex-shrink-0"]/ul[@class="list-style-none d-flex"]/li/a/span/strong/text()')[
    0]
print("project_commit_number", project_commit_number)
project_branch = tree.xpath('//*[@id="branch-select-menu"]/summary/span[1]/text()')[0].strip()
print("project_branch", project_branch)  # //*[@id="repo-content-pjax-container"]/div/div[2]/div[2]/div/div[1]/div/p
project_describe = tree.xpath('//*[@id="repo-content-pjax-container"]/div/div[2]/div[2]/div/div[1]/div/p//text()')
if project_describe is None or project_describe == "" or project_describe is []:
    project_describe = "Null"
else:
    project_describe = "".join([project_describe[i].strip() for i in range(len(project_describe))])
    project_describe = re.sub(r"\W+", " ", project_describe)
    print("project_describe",
          project_describe)  # //*[@id="repo-content-pjax-container"]/div/div[2]/div[2]/div/div[1]/div/div[1]/div
project_label = tree.xpath(
    '//*[@id="repo-content-pjax-container"]/div/div[2]/div[2]/div/div[1]//div[@class="f6"]//text()')
project_label = "".join([project_label[i].strip() + r"/" for i in range(len(project_label))])
print("project_label", project_label)  # //*[@id="repo-content-pjax-container"]/div/div[2]/div[2]/div//div/ul
project_languages = tree.xpath(
    '//*[@id="repo-content-pjax-container"]/div/div[2]/div[2]/div//div[@class="BorderGrid-cell"]/ul[@class="list-style-none"]/li[@class="d-inline"]//text()')
if project_languages == None or project_languages == "":
    project_languages = "Null"
else:
    project_languages = [project_languages[i].strip() for i in range(len(project_languages))]
    project_languages = "".join(project_languages)  # .split("%")
    # project_languages.pop()
    print("project_languages", project_languages)
    # github_href = 'https://github.com'
# project_clone_https =
# li_lst = tree.xpath('//*[@id="repository-container-header"]/div[1]/ul/li')
# for li in li_lst:
#     print(li.xpath('.//text()'))
