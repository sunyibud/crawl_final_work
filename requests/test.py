# -*- coding: UTF-8 -*-
# @Time : 2021/12/04
# @Author : Sunyi
# @File : est.py
# @Detail : 
import requests


def main():
    headers = {
        'accept': 'text/fragment+html',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
        'cache-control': 'no-cache',
        'cookie': '_octo=GH1.1.1185250697.1622521991; _device_id=e16604776f20c07cc438d49f3b443b6c; user_session=g_pUgQ26hBXQm3dqDu_Gby2X0ZEA2qhxSTL0dq3aPbHNW3TF; __Host-user_session_same_site=g_pUgQ26hBXQm3dqDu_Gby2X0ZEA2qhxSTL0dq3aPbHNW3TF; logged_in=yes; dotcom_user=Sunyi-20011; color_mode=%7B%22color_mode%22%3A%22auto%22%2C%22light_theme%22%3A%7B%22name%22%3A%22dark_dimmed%22%2C%22color_mode%22%3A%22dark%22%7D%2C%22dark_theme%22%3A%7B%22name%22%3A%22dark%22%2C%22color_mode%22%3A%22dark%22%7D%7D; tz=Asia%2FShanghai; has_recent_activity=1; _gh_sess=J9cQs9771sfLMPNOP9delej5ygvRgA5wrZ2DsNDCUzYEwlSWDehc%2B%2FJcMXDbIn2HLhVuLhazoNPOqHPdsayOE7%2Bxg1pjzLcxXRQnwj3%2FIDctwhGiTX93GekZ67j3wD6oTTHPmbbon3zbfhj1TV5L6cueh37niGEpAX8p2zHKQSV8uuu5Q9RZ0hLqFc9g6iOc8%2B1oC%2Blfg8IOVbXbbGcvhtpzWV4g8i1HrQF2Z9AhAw1tgAzD1yunWo18paVaatQdDYpWxifl1H4Uv86JVa1W16lSCyEPLmPp%2BE6%2FAaCJZbfeS0Q7Ox46DoWEg7Wf51hTafO0w5fJ2ggS%2FEIN1PAd7QtCqYl%2FQTM9q%2FSN0a7ouTW4HB3OBJ%2FIxFAB3so%3D--4qgnHF3W6bol5nqg--O9pz2JlAVcpjaTmlW0LAqA%3D%3D',
        'dnt': '1',
        'pragma': 'no-cache',
        'referer': 'https://github.com/hakimel/Ladda',
        'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="96", "Google Chrome";v="96"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36',
        'x-requested-with': 'XMLHttpRequest'
    }
    resp = requests.get("https://github.com/hakimel/Ladda", headers)
    with open("test.html", 'w', encoding='utf-8') as fp:
        fp.write(resp.text)


if __name__ == "__main__":
    main()
