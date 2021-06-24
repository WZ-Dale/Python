# @License : 西安工业大学
# @Author  : 王泽 WZ-Dale
# @Time    : 2021/6/22 10:09

"""视频网站工作原理"""
# <video src="视频.mp4"></video>      # 不能这么干
# 一般网站是这么做的：
# 用户上传 -> 转码（把视频做处理，做成不同清晰度的（如2K，1080，标清）） -> 切片处理（把单个文件进行拆分，拆分成的单个文件小于10s）
# 用户在进行拉动进度条的时候，可播放
# ==========================
# 需要一个文件记录：1.视频播放顺序；2.视频存放的路径。
# 拆分好的文件记录到M3U（如同txt、json）都是文本
# M3U8（M3U文件经过"utf-8"编码得到的）

# 想要抓取一个视频：
# 1.找的M3U8文件（通过各种手段找）
# 2.通过M3U8下载到ts文件（切片文件）
# 3.可以通过各种手段（不仅是编程手段，有时可能要用到Pr）把ts文件合并成一个mp4文件

"""抓取91看剧_简单版"""
# 网页源码中没有<video>标签，说明<video>标签是通过js脚本动态生成的
# 流程：
# 1.拿到页面源代码
# 2.从源代码中提取到m3u8的url
# 3.下载m3u8
# 4.读取m3u8文件，下载切片
# 5.合并视频

import requests
import re

# url = "https://91kanju.com/vod-play/54812-1-1.html"
# resp = requests.get(url)
# # print(resp.text)
# obj = re.compile(r"url: '(?P<url>.*?)',", re.S)     # 用来提取m3u8的url地址
# m3u8_url = obj.search(resp.text).group("url")
# # print(m3u8_url)
# resp.close()
# resp1 = requests.get(m3u8_url)
# with open("哲仁王后.m3u8", mode="wb") as f:
#     f.write(resp1.content)
# resp1.close()
# print("m3u8文件下载成功！")

# 解析m3u8文件
with open("哲仁王后.m3u8", mode="r", encoding="utf-8") as f:
    n = 1
    for line in f:
        line = line.strip()     # 去掉空格、空白、换行符
        if line.startswith("#"):    # 如果以#开头，不需要处理该行
            continue
        # print(line)
        # 下载视频片段
        resp2 = requests.get(line)
        f1 = open(f"video1/{n}.ts", mode="wb")
        f1.write(resp2.content)
        f1.close()
        resp2.close()
        print(f"第{n}个片段下载成功！")
        n += 1

# 接下来只需要使用其它视频合并工具对视频进行合并即可
