# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ScrapyFinalWorkItem(scrapy.Item):
    project_belong_topic = scrapy.Field()  # 仓库所属类别
    project_topic_project_number = scrapy.Field()  # 类别所含的项目数量
    project_topic_describe = scrapy.Field()  # topic描述
    project_owner = scrapy.Field()  # 仓库拥有者
    project_name = scrapy.Field()  # 仓库名称
    project_path = scrapy.Field()  # 仓库路径
    project_star = scrapy.Field()  # 项目获得的star数量
    project_fork = scrapy.Field()  # 项目获得的fork数量
    project_revise_time = scrapy.Field()  # 项目最后修改的时间
    project_commit_number = scrapy.Field()  # 项目提交的次数
    project_branch = scrapy.Field()  # 当前界面的项目分支名
    project_describe = scrapy.Field()  # 项目的描述
    project_label = scrapy.Field()  # 项目的标签
    project_languages = scrapy.Field()  # 项目中所使用的语言及百分比
    project_clone_ssh = scrapy.Field()  # 项目的 ssh 连接
    project_download_zip = scrapy.Field()  # 项目的 zip 链接
    Topic_name = scrapy.Field()  # 类别名
    topic_number = scrapy.Field()  # 类别所含的项目数量
    topic_describe = scrapy.Field()  # topic描述
