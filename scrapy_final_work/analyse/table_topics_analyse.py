# -*- coding: UTF-8 -*-
# @Time : 2021/12/04
# @Author : Sunyi
# @File : topic_projects.py
# @Detail : 板块包含项目数最高的前十个
import imageio

from scrapy_final_work.analyse.DB import DB
import matplotlib.pyplot as plt
from matplotlib.pyplot import MultipleLocator
import numpy as np
import wordcloud
import jieba


def modules_projects_num_zzt(topics):
    print("正在绘制模块所含项目数前十的柱状图")
    sorted_topics = sorted(topics, key=lambda keys: int(keys[1]), reverse=True)
    topic_top10 = []
    project_num_top10 = []
    for sorted_topic in sorted_topics[:10]:
        topic_top10.append(sorted_topic[0])
        project_num_top10.append(int(sorted_topic[1]))
    print('topic_top10:', topic_top10)
    print('project_num_top10:', project_num_top10)
    print('开始绘制模块-项目数柱状图...')
    plt.rcParams["font.family"] = "KaiTi"
    plt.title("各模块项目数")
    y = project_num_top10
    x = np.arange(len(y))
    x_ticks = topic_top10
    plt.xticks(x, x_ticks, rotation=20)
    plt.xlabel('模块名称')
    plt.ylabel('项目数')
    rects = plt.bar(x, y)
    for rect in rects:
        height = rect.get_height()
        plt.annotate('{}'.format(height),
                     xy=(rect.get_x() + rect.get_width() / 2, height),
                     xytext=(0, 3),  # 3 points vertical offset
                     textcoords="offset points",
                     ha='center', va='bottom')
    plt.savefig("./results/module_project_zzt.png")  # 保存图像
    print("绘制成功")
    # plt.show()


def modules_desc_cy(topics):
    print("正在绘制板块描述词云...")
    desc_str = ""
    for topic in topics:
        desc_str += topic[3]
    with open("./results/module_desc_str.txt", 'w', encoding='utf-8') as fp:
        fp.write(desc_str)
    mk = imageio.imread("./results/github1.png")
    w = wordcloud.WordCloud(mask=mk)
    # 构建词云对象w，设置词云图片宽、高、字体、背景颜色等参数
    w = wordcloud.WordCloud(background_color='white', contour_width=1,
                            contour_color='steelblue', font_path='msyh.ttc', mask=mk)
    txt_list = jieba.lcut(desc_str)
    string = "".join(txt_list)
    w.generate(string)

    # 将生成的词云保存为output2-poem.png图片文件，保存到当前文件夹中
    w.to_file('./results/module_desc_cy.png')
    print("绘制成功")


def main():
    db = DB("root", "Zx4653397..", "github")
    topics_data = db.search('select * from Topics')
    all_topics = []
    topics = []
    for topic in topics_data:
        if topic[1] in all_topics:
            continue
        all_topics.append(topic[1])
        topics.append(topic[1:])
    modules_projects_num_zzt(topics)
    modules_desc_cy(topics)
    db.close()


if __name__ == "__main__":
    main()
