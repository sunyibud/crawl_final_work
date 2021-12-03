# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ScrapyFinalWorkItem(scrapy.Item):
    project_path = scrapy.Field()  # 仓库路径
    project_star = scrapy.Field()  # 项目获得的star数量
    project_fork = scrapy.Field()  # 项目获得的fork数量
    project_revise_time = scrapy.Field()  # 项目最后修改的时间
    project_commit_number = scrapy.Field()  # 项目提交的次数
    project_branch = scrapy.Field()  # 当前界面的项目分支名
    project_describe = scrapy.Field()  # 项目的描述
    project_label = scrapy.Field()  # 项目的标签
    project_languages = scrapy.Field()  # 项目中所使用的语言及百分比
