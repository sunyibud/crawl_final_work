# import pygal
import pygal_maps_world.maps

# worldmap_chart = pygal.maps.world.World()
worldmap_chart = pygal_maps_world.maps.World()
worldmap_chart.title = "世界范围内的数据采集"
worldmap_chart.add("搞个der", {
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
worldmap_chart.add("中", {
    "ca",
    "it",
    "br",
    "th",
    "ar",
    "co",
    "pt",
    "pk",
    "pl",
    "bd",
    "se",
    "tr",
    "ve",
    "gb",
})
worldmap_chart.add("低", {
    "nl",
    "hu",
    "cl",
    "ph",
    "my",
    "kr",
    "uy",
    "ro",
    "eg",
    "ke",
    "kp",
    "cz",
    "sk",
    "mg",
})
worldmap_chart.render_to_file('数据采集.svg')
