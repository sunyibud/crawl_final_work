# -*- coding: UTF-8 -*-
# @Time : 2021/12/04
# @Author : Sunyi
# @File : test.py
# @Detail : 

import pygal

worldmap_chart = pygal.maps.world.World()
worldmap_chart.title = "一个虚拟的2018年Android手机全球销量地图"
worldmap_chart.add("2018年", {
    "cn": 6500,
    "us": 6000,
    "de": 5500,  # 德国
    "jp": 5000,
    "in": 4500,  # 印度
    "ru": 4000,  # 俄国
    "fr": 3500,  # 法国
    "hk": 3000,
    "tw": 2500,
    "it": 2000,  # 意大利
    "kr": 1500,  # 韩国
    "mo": 1000,  # Macao，澳门
    "gb": 500,  # United Kingdom，英国
})
worldmap_chart.render_to_file('bar_chart.svg')
