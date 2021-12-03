import re
from ..items import ScrapyFinalWorkItem
import scrapy


# 若未正常获得时间则从文件最近修改的时间来获取
def Judgement_Date(file_revise_time):
    # 月份英语简称
    month = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    # 将每个文件修改的时间进行切割
    file_revise_time = [re.split(r"\s+", re.sub(r"[,\s+]", " ", file_revise_time[i])) for i in
                        range(len(file_revise_time))]
    # 第一次按修改时间中的年份进行从大到小的排序
    file_revise_time = sorted(file_revise_time, key=lambda x: x[2], reverse=True)
    # print("1", file_revise_time)

    # 判断属于最新年份的修改日期并将其切割出来
    for revise_time in file_revise_time:  # [month, day, year]
        if not revise_time[2] == file_revise_time[0][2]:
            # 不是最新年份第一次出现的下标
            dif_year = file_revise_time.index(revise_time)
            # 切割列表，使列表中的元素都是最新的年份
            file_revise_time = file_revise_time[:dif_year]
            break
    # print("2", file_revise_time)

    # 将月份的英文简称替换成所对应的下标
    for i in range(len(file_revise_time)):
        file_revise_time[i][0] = month.index(file_revise_time[i][0])

    # 在最新的列表中按月对齐排序
    file_revise_time = sorted(file_revise_time, key=lambda x: x[0], reverse=True)
    # print("3", file_revise_time)

    # 判断属于最晚日期的修改日期并将其切割出来
    for revise_time in file_revise_time:  # [month, day, year]
        if not revise_time[0] == file_revise_time[0][0]:
            # 将不同的第一次出现的下标记录下来
            dif_month = file_revise_time.index(revise_time)
            # 切割列表使其中的元素都处于同年同月
            file_revise_time = file_revise_time[:dif_month]
            break
    # print("4", file_revise_time)

    # 在同月中按照最近的天数进行排序
    file_revise_time = sorted(file_revise_time, key=lambda x: x[1], reverse=True)

    # 将月份从数字重新变成英文简写
    for i in range(len(file_revise_time)):
        file_revise_time[i][0] = month[file_revise_time[i][0]]
    print("5", file_revise_time)

    if file_revise_time == "" or file_revise_time is None or len(file_revise_time) == 0:
        return "Null"
    else:
        # 保存至相同的格式
        nealy_time = " ".join(file_revise_time[0])
        if nealy_time == "" or nealy_time is None:
            nealy_time = "Null"
        return nealy_time


class GithubSpider(scrapy.Spider):
    name = 'github'
    # allowed_domains = ['www.xx']
    start_urls = ['https://github.com/explore']  #
    # github起始位置
    github_Href = "https://github.com/"
    # 每个板块需要爬取的项目数量
    topic_number = 100
    allow_number = 0

    # 获取每个板块的信息
    def parse_get_topics(self, response):
        div_lst = response.xpath('//*[@id="js-pjax-container"]/div[4]/div[1]/div/div')  # 获取每个板块的div
        for div in div_lst:  # 循环获取板块里面的url
            self.allow_number += 1
            # print("div", div)
            # print("测试是否进行")
            dic = {}
            dic['href'] = r'https://github.com' + div.xpath('./a[1]/@href').extract_first().strip()
            dic['href'] = dic['href'] + "?o=desc&s=stars"
            dic['name'] = div.xpath('./a[1]/div/div/p[1]/text()').extract_first().strip()
            dic['describe'] = div.xpath('./a[1]/div/div/p[2]/text()').extract_first().strip()
            # print(dic)
            # 进入分区
            yield scrapy.Request(url=dic['href'], callback=self.parse_get_topic_info, meta={"dic": dic})
            # if self.allow_number > 2:
            #     break
            break

    # 获取每个板块内项目的信息
    def parse_get_topic_info(self, response):
        print("测试进入parse_get_topic_info")
        # 界面详情介绍
        detail_describe = response.xpath(
            '//*[@id="js-pjax-container"]/div[2]/div[2]/div/div[1]/div[1]/div/p/text()').extract_first()
        # print(detail_describe)
        # 获取当前板块的所有项目数
        topic_project_number = response.xpath(
            '//*[@id="js-pjax-container"]/div[2]/div[2]/div/div[1]/h2//text()').extract_first()
        # 对获取的数据进行进一步清洗
        obj_number = re.compile(r"\d+")
        # 连接列表
        topic_project_number = "".join(obj_number.findall(topic_project_number)).strip()
        # print(topic_project_number)
        # 获取当前页的所有项目的列表
        article_lst = response.xpath('//*[@id="js-pjax-container"]/div[2]/div[2]/div/div[1]/article')
        # print(div_project_lst)
        for article in article_lst:
            # 获取项目的路径
            project_path = article.xpath('./div[@class="px-3"]//h3//text()').extract()
            # 对获取的项目路径列表进行数据清洗
            project_path = [project_path[i].strip().replace(" ", "") for i in range(len(project_path))]
            project_path = "".join(project_path).strip()
            # 获取仓库所属用户名
            project_username = project_path.split("/")[0]
            # print("project_username", project_username)
            # 获取仓库名字
            project_name = project_path.split("/")[-1]
            # print("project_name", project_name)
            # 拼接仓库链接
            project_url = self.github_Href + project_path
            # 获得clone的 https 链接
            project_clone_https = project_url + ".git"
            # print("project_clone_https", project_clone_https)
            # 获得clone的 ssh 链接
            project_clone_ssh = "git@github.com:" + project_path + ".git"
            # print("project_clone_ssh", project_clone_ssh)
            yield scrapy.Request(url=project_url, callback=self.parse_project_detail_info,
                                 meta={"project_path": project_path})
            # break

    # 获得每个项目内的具体信息
    def parse_project_detail_info(self, response):
        project_path = response.meta["project_path"]
        print("测试是否进入parse_project_detail_info")
        # 获得 star 与 fork 的数量标签
        project_li_line = response.xpath('//*[@id="repository-container-header"]/div[1]/ul/li')
        # print("project_li_line", project_li_line.extract())
        # 初始化star fork
        project_star, project_fork = 0, 0
        for li in project_li_line:
            # print("li.extract()", li.extract())
            # print("li.text().extract()", li.xpath(".//text()").extract())
            # 获得标签下面的文本
            temp = li.xpath('.//text()').extract()
            # print(temp)
            # 拼接字符串
            temp = "".join([temp[i].strip() for i in range(len(temp))])
            # print("temp:", temp)
            # 判断当前的 li 标签是否属于 star
            if "Star" in temp:
                project_star = "".join(re.findall(r"[.\d+]", temp))  # 利用re将数字提取出来
                # 判断数量是否超过一千
                if temp[-1] == "k":
                    project_star += "k"
                continue
            # 判断当前的 li 标签是否属于 fork
            if "Fork" in temp:
                project_fork = "".join(re.findall(r"[.\d+]", temp))  # 利用re将数字提取出来
                # 判断数量是否超过一千
                if temp[-1] == "k":
                    project_fork += "k"
                continue
        # print("project_star", project_star)
        # print("project_fork", project_fork)
        # 获取最后修改时间
        project_revise_time = response.xpath(
            '//*[@id="repo-content-pjax-container"]/div/div[2]/div[1]/div[2]/div[1]/div/div[2]/div[2]//relative-time/text()').extract_first()
        # //*[@id="repo-content-pjax-container"]/div/div[2]/div[1]/div[2]/div[1]/div/div[2]/div[2]//relative-time/text()
        # 判断获取的是否为空
        if project_revise_time is None or len(project_revise_time) == 0 or project_revise_time == "":
            print("进入获得时间格式if")
            # 如果没有从主页获得则从文件修改时间获取
            project_final_revise_time_list = response.xpath(
                '//*[@id="repo-content-pjax-container"]/div/div[2]/div[1]/div[2]/div[3]/div[1]/div[@role="row"]//time-ago/text()').extract()
            print("project_final_revise_time_list", project_final_revise_time_list)
            # 将时间设置为文件最后修改时间
            project_revise_time = Judgement_Date(project_final_revise_time_list)
        else:
            # 如果不为空，则对数据格式进行修改将其从 "month day, year"格式变为 "month day year"
            print("进入修改时间格式else")
            project_revise_time = re.split(r"[,\s+]", project_revise_time)
            project_revise_time.remove("")
            project_revise_time = " ".join(project_revise_time)
        # print("project_revise_time", project_revise_time)
        # 获取总共提交的数量
        project_commit_number = response.xpath(
            '//*[@id="repo-content-pjax-container"]/div/div[2]/div[1]/div[2]/div[1]/div/div[@class="flex-shrink-0"]/ul[@class="list-style-none d-flex"]/li/a/span/strong/text()').extract_first()
        # print("project_commit_number", project_commit_number)
        # 获取当前界面的分支名
        project_branch = response.xpath('//*[@id="branch-select-menu"]/summary/span[1]/text()').extract_first()
        # 去除获得的分支前后的空格
        project_branch = project_branch.strip()
        # print("project_branch", project_branch)
        # 获得项目的 zip 下载链接 例如https://github.com/marktext/marktext/archive/refs/heads/develop.zip
        project_download_zip = self.github_Href + project_path + "/archive/refs/heads/" + project_branch + ".zip"
        # print("project_download_zip", project_download_zip)
        # 获取此项目的描述
        project_describe = response.xpath(
            '//*[@id="repo-content-pjax-container"]/div/div[2]/div[2]/div/div[1]/div/p//text()').extract()
        # 判断得到的项目描述是否为空
        if project_describe is None or project_describe == "" or project_describe is [] or len(project_describe) == 0:
            project_describe = "Null"
        else:
            # 拼接字符串
            project_describe = "".join([project_describe[i].strip() for i in range(len(project_describe))])
            # 对提取到的一些特殊图标进行去除，但是因为会去除标点符号，所以将特殊图片替换成空格
            project_describe = re.sub(r"\W+", " ", project_describe)
        # print("project_describe", project_describe)
        # 获取项目标签
        project_label = response.xpath(
            '//*[@id="repo-content-pjax-container"]/div/div[2]/div[2]/div/div[1]//div[@class="f6"]//text()').extract()
        # 拼接项目标签，使用 “/” 分割不同标签
        project_label = "".join([project_label[i].strip() + r"/" for i in range(len(project_label))])
        # print("project_label", project_label)
        # 获取项目所涉及语言及该语言在项目中所占百分比 例如 javascript 57.3%
        project_languages = response.xpath(
            '//*[@id="repo-content-pjax-container"]/div/div[2]/div[2]/div//div[@class="BorderGrid-cell"]/ul[@class="list-style-none"]/li[@class="d-inline"]//text()').extract()
        # 判断获取的语言是否为空
        if project_languages is None or project_languages == "" or project_languages is [] or len(
                project_languages) == 0:
            project_languages = "Null"
        else:
            # 将空格以及换行符去除
            project_languages = [project_languages[i].strip() for i in range(len(project_languages))]
            # 拼接字符串
            project_languages = "".join(project_languages)  # .split("%")
            # project_languages.pop()
        # print("project_languages", project_languages)
        item = ScrapyFinalWorkItem()
        item["project_path"] = project_path  # 仓库路径
        item["project_star"] = project_star  # 项目获得的star数量
        item["project_fork"] = project_fork  # 项目获得的fork数量
        item["project_revise_time"] = project_revise_time  # 项目最后修改的时间
        item["project_commit_number"] = project_commit_number  # 项目提交的次数
        item["project_branch"] = project_branch  # 当前界面的项目分支名
        item["project_describe"] = project_describe  # 项目的描述
        item["project_label"] = project_label  # 项目的标签
        item["project_languages"] = project_languages  # 项目中所使用的语言及百分比
        yield item

    def parse(self, response):
        kinds_lst = response.xpath('//*[@id="js-pjax-container"]/div[1]/nav/div/a/@href').extract()
        Explore_Href = self.github_Href + kinds_lst[0]  # explore 界面
        Topics_Href = self.github_Href + kinds_lst[1]  # topics 界面
        Trending_Href = self.github_Href + kinds_lst[2]  # trending 界面
        Collection_Href = self.github_Href + kinds_lst[3]  # Collections 界面
        events = self.github_Href + kinds_lst[4]  # events 界面
        # print(kinds_lst)
        # 进入 topics 界面
        yield scrapy.Request(url=Topics_Href, callback=self.parse_get_topics)
