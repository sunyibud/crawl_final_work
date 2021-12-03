# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import traceback
import time
from itemadapter import ItemAdapter
import logging


class ScrapyFinalWorkPipeline:
    fp = None
    f_log = None
    logging.basicConfig(stream=f_log,
                        format='%(asctime)s - %(name)s - %(levelname)s - %(module)s - %(message)s',
                        datefmt='%Y%m%d%H%M%S',
                        level=10)  # 当前配置表示 10分以上的分数会被写入文件

    def open_spider(self, spider):
        print("开始爬虫....")
        localtime = time.localtime()
        format_time = '%Y-%m-%d_%H—%M—%S'
        cur_time = time.strftime(format_time, localtime)
        self.fp = open(f'./{cur_time}.txt', 'w', encoding='utf-8')
        self.f_log = open('./githubinfo.log', 'a', encoding='utf-8')

    def process_item(self, item, spider):
        project_path = item["project_path"]  # 仓库路径
        project_star = item["project_star"]  # 项目获得的star数量
        project_fork = item["project_fork"]  # 项目获得的fork数量
        project_revise_time = item["project_revise_time"]  # 项目最后修改的时间
        project_commit_number = item["project_commit_number"]  # 项目提交的次数
        project_branch = item["project_branch"]  # 当前界面的项目分支名
        project_describe = item["project_describe"]  # 项目的描述
        project_label = item["project_label"]  # 项目的标签
        project_languages = item["project_languages"]  # 项目中所使用的语言及百分比
        try:
            temp = project_path + " " + project_star + " " + project_fork + " " + project_revise_time + " " + project_commit_number + " " + project_branch + " " + project_describe + " " + project_label + " " + project_languages + "\n"
            self.fp.writelines(temp)
        except:
            logging.error(traceback.format_exc())
        return item

    def close_spider(self, spider):
        print("结束爬虫....")
        self.fp.close()
        self.f_log.close()
