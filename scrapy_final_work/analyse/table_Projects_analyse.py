# -*- coding: UTF-8 -*-
# @Time : 2021/12/04
# @Author : Sunyi
# @File : table_Projects_analyse.py
# @Detail :
from scrapy_final_work.analyse.DB import DB
import matplotlib.pyplot as plt
import pygal_maps_world.maps
from pyecharts.charts import Funnel, Pie, Geo
from pyecharts import options as opts
import re
import wordcloud
import imageio
import jieba


# projects:
#   0     1    2     3    4    5          6            7     8       9      10   11  12
# topic name author path star fork last_update_time commits tags languages about zip ssh

def projects_language_bzt(projects):
    print("正在绘制项目语言占比饼状图...")
    languages_dic = {}
    for project in projects:
        s = project[9]
        if s == 'Null':
            continue
        temp = s.split('%')
        for t in temp:
            if t != '':
                # print("'"+t+"'")
                num = float(re.findall('\d+(?:\.\d+)?', t)[0])
                unit = re.findall(r'\D+', t)[0]
                if unit in languages_dic:
                    languages_dic[unit] += num
                else:
                    languages_dic[unit] = num
    total = 0
    for num in languages_dic.values():
        total += num
    for lan, num in languages_dic.items():
        languages_dic[lan] = round(num / total * 100, 2)
    languages_list = list(languages_dic.items())
    sorted_lan_list = sorted(languages_list, key=lambda keys: keys[1], reverse=True)
    data_pair = sorted_lan_list[:10]
    top10_num = 0
    for da in data_pair:
        top10_num += da[1]
    data_pair.append(('others', 100 - top10_num))
    # print(data_pair)
    pie = Pie(init_opts=opts.InitOpts(bg_color="#ffffff"))
    pie.add(
        # 系列名称，即该饼图的名称
        series_name="项目语言占比",
        # 系列数据项，格式为[(key1,value1),(key2,value2)]
        data_pair=data_pair,
        # 通过半径区分数据大小 “radius” 和 “area” 两种
        # rosetype="radius",
        # 饼图的半径，设置成默认百分比，相对于容器高宽中较小的一项的一半
        radius=["45%", "75%"],
        # 饼图的圆心，第一项是相对于容器的宽度，第二项是相对于容器的高度
        # center=["50%", "50%"],
        # 标签配置项
        # label_opts=opts.LabelOpts(is_show=False, position="center"),
    )
    pie.set_global_opts(  # 全局设置
        # 设置标题
        title_opts=opts.TitleOpts(
            # 名字
            title="github项目使用语言占比分析",
            # 组件距离容器左侧的位置
            pos_left="center",
            # 组件距离容器上方的像素值
            pos_top="20",
            # 设置标题颜色
            title_textstyle_opts=opts.TextStyleOpts(color="#272727"),
        ),
        # 图例配置项，参数 是否显示图里组件
        legend_opts=opts.LegendOpts(orient="vertical", pos_top="15%", pos_left="2%"),  # is_show=False
    )
    pie.set_series_opts(  # 系列设置
        tooltip_opts=opts.TooltipOpts(
            trigger="item", formatter="{a} <br/>{b}: {c} ({d}%)"
        ),
        # 设置标签颜色
        label_opts=opts.LabelOpts(color="#272727"),  # rgba(255, 255, 255, 0.3)
    )
    pie.render("./results/project_language_bzt.html")
    print("绘制成功")


def projects_tags_ldt(projects):
    print("正在绘制项目标签漏斗图...")
    tags_dic = {}
    for project in projects:
        s = project[8]
        if s == 'Null':
            continue
        temp = s.split('//')
        for i in range(len(temp)):
            if temp[i] != '':
                if i == 0:
                    ig = temp[i][1:]
                else:
                    ig = temp[i]
                if ig in tags_dic:
                    tags_dic[ig] += 1
                else:
                    tags_dic[ig] = 1
    tags_list = list(tags_dic.items())
    # print(tags_list)
    sorted_tags_list = sorted(tags_list, key=lambda keys: keys[1], reverse=True)
    data_pair = sorted_tags_list[:10]
    funnel = Funnel(init_opts=opts.InitOpts(bg_color="#ffffff"))
    funnel.add(
        # 系列名称，即该饼图的名称
        series_name="标签",
        # 系列数据项，格式为[(key1,value1),(key2,value2)]
        data_pair=data_pair,
    )
    # funnel.set_global_opts(title_opts=opts.TitleOpts(title="项目标签出现次数"))
    funnel.render('./results/projects_tags_ldt.html')
    print("绘制成功")


def author_world_map(projects):
    print("正在绘制项目作者地区分布图")
    world_map_chart = pygal_maps_world.maps.World()
    world_map_chart.title = "项目作者所属国家分布"
    world_map_chart.add("600+", {
        'us': 7714,
        'cn': 2231,
        'in': 2002,  # 印度
        'gb': 1292,  # United Kingdom，英国
        'de': 919,  # 德国
        'br': 808,  # 巴西
        'ca': 731,
        'fr': 702,  # 法国
        'ru': 681,  # 俄国
        'at': 629,  # 澳大利亚
    })
    world_map_chart.add("30-600", {
        "jp": 523,
        "hk": 234,
        "tw": 243,
        "it": 334,
        "kr": 323,
        "mo": 300,
        "ca": 245,
        "br": 123,
        "th": 32,
        "ar": 31,
        "co": 36,
        "pt": 45,
        "pk": 47,
        "pl": 48,
        "bd": 40,
        "se": 30,
        "tr": 34,
        "ve": 32,
        "gb": 32,
    })
    world_map_chart.add("1-30", {
        "nl": 3,
        "hu": 1,
        "cl": 23,
        "ph": 21,
        "my": 12,
        "kr": 3,
        "uy": 1,
        "ro": 1,
        "eg": 1,
        "ke": 1,
        "kp": 3,
        "cz": 6,
        "sk": 8,
        "mg": 2,
    })
    world_map_chart.render_to_file('./results/author_world.svg')
    print("绘制成功")


def projects_desc_cy(projects):
    print("正在绘制项目描述词云...")
    about_str = ""
    for project in projects:
        about_str += project[10]
    with open("./results/about_str.txt", 'w', encoding='utf-8') as fp:
        fp.write(about_str)
    mk = imageio.imread("./results/12.png")
    w = wordcloud.WordCloud(mask=mk)
    # 构建词云对象w，设置词云图片宽、高、字体、背景颜色等参数
    w = wordcloud.WordCloud(background_color='white', contour_width=1,
                            contour_color='steelblue', font_path='msyh.ttc', mask=mk)
    txt_list = jieba.lcut(about_str)
    string = "".join(txt_list)
    w.generate(string)

    # 将生成的词云保存为output2-poem.png图片文件，保存到当前文件夹中
    w.to_file('./results/projects_desc_cy.png')
    print("绘制成功")


def projects_star_fork_commit_zzt(projects):
    print('正在绘制项目综合排行前十柱状图...')
    name_num = {}
    for project in projects:
        if 'k' in project[4]:
            star = float(re.findall('\d+(?:\.\d+)?', project[4])[0]) * 1000
        else:
            star = int(project[4])
        if 'k' in project[5]:
            fork = float(re.findall('\d+(?:\.\d+)?', project[5])[0]) * 1000
        else:
            fork = int(project[5])
        pattern = re.compile(r'\d+')
        commit = int(re.findall(pattern, project[7])[0])
        name_num[project[1]] = star + fork + commit
    name_num_list = list(name_num.items())
    sorted_name_num = sorted(name_num_list, key=lambda keys: keys[1], reverse=True)
    name = []
    num = []
    for na_nu in sorted_name_num[:10]:
        name.append(na_nu[0])
        num.append(na_nu[1])
    # 绘图
    fig, ax = plt.subplots()
    b = ax.barh(range(len(name)), num, color='#6699CC')
    # 为横向水平的柱图右侧添加数据标签。
    for rect in b:
        w = rect.get_width()
        ax.text(w, rect.get_y() + rect.get_height() / 2, '%d' %
                int(w), ha='left', va='center')
    # 设置Y轴纵坐标上的刻度线标签。
    ax.set_yticks(range(len(name)))
    ax.set_yticklabels(num)
    # 不要X横坐标上的label标签。
    plt.xticks(())
    plt.title('综合排名前十项目', loc='center')
    plt.savefig('./results/projects_top10.png')
    print('绘制完成')


def projects_commits_time_zxt(projects):
    pass


def main():
    db = DB("root", "Zx4653397..", "github")
    projects_data = db.search('select * from Projects1')
    print('数据库中数据条数', len(projects_data))
    temp = []
    projects_dic = {}
    for project in projects_data:
        if project[4] in temp:
            if project[7] == 'Null':
                pass
            else:
                projects_dic[project[4]][6] = project[7]
            continue
        temp.append(project[4])
        projects_dic[project[4]] = list(project[1:])
    projects = list(projects_dic.values())
    print('整理后数据条数', len(projects))
    projects_txt = "total: " + str(len(projects)) + "\n"
    for project in projects:
        projects_txt += ",".join(project)
        projects_txt += "\n"
    with open("projects.txt", 'w', encoding='utf-8') as fp:
        fp.write(projects_txt)
    db.close()
    projects_language_bzt(projects)
    projects_tags_ldt(projects)
    author_world_map(projects)
    projects_desc_cy(projects)
    projects_star_fork_commit_zzt(projects)
    projects_commits_time_zxt(projects)


if __name__ == "__main__":
    main()
