# @License : 西安工业大学
# @Author  : 王泽 WZ-Dale
# @Time    : 2021/5/11 14:12

"""1.小爬虫"""
# from urllib.request import urlopen
#
# url = "http://www.baidu.com"
# resp = urlopen(url)
# with open("baidu.html", mode='w', encoding='utf-8') as f:
#     f.write(resp.read().decode("utf-8"))
# print("over!")

"""2.获取网页源码"""
# import requests
#
# url="https://www.baidu.com/s?wd=刘德华"
# head={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3868.400 QQBrowser/10.8.4394.400"}
# resp=requests.get(url, headers=head)
# print(resp)
# print(resp.text)

"""3.获取百度翻译结果"""
# import requests
#
# url="https://fanyi.baidu.com/sug"
# s=input("请输入你要翻译的英文单词：")
# dat={"kw":s}
# resp=requests.post(url, data=dat)
# print(resp.json())  # 将服务器返回的内容直接处理成json() => dict

"""4.爬取喜剧榜"""
# import requests
#
# url="https://movie.douban.com/j/chart/top_list"
# param={
#     "type": "24",
#     "interval_id": "100:90",
#     "action": "",
#     "start": 0,
#     "limit": 20,
# }
# head={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3868.400 QQBrowser/10.8.4394.400"}
# resp=requests.get(url, param, headers=head)
# # print(resp.request.headers)
# print(resp.json())
# resp.close()

"""5.re解析（正则表达式）"""
# import re
#
# lst=re.findall(r"\d+", "电话：110， 号码：120")
# print(lst)
# it=re.finditer(r"\d+", "电话：110，号码：120")
# print(it)
# for i in it:
#     print(i.group())  # 从迭代器中拿内容
#
# s=re.search(r"\d+", "电话：110，号码：120")  # 全文匹配
# print(s.group())
# # s=re.match(r"\d+", "电话：110，号码：120")  # 从头开始匹配
# # print(s.group())
# s=re.match(r"\d+", "110，号码：120")  # 从头开始匹配
# print(s.group())
#
# # 预加载正则表达式（提高效率）
# obj=re.compile(r"\d+")
# ret=obj.finditer("电话：110，号码：120")
# for i in ret:
#     print(i.group())
#
# s="""
# <div class='jay'><span id='1'>郭麒麟</span></div>
# <div class='jj'><span id='2'>宋铁</span></div>
# <div class='jolin'><span id='3'>大聪明</span></div>
# <div class='sylar'><span id='4'>范思哲</span></div>
# <div class='tory'><span id='5'>胡说八道</span></div>
# """
# # (P<分组名字>正则)  可以单独从正则匹配的内容中进一步提取内容
# obj=re.compile(r"<div class='.*?'><span id='(?P<num>\d+)'>(?P<ren>.*?)</span></div>", re.S)  #re.S：让.能匹配换行符
# res=obj.finditer(s)
# for i in res:
#     print(i.group("num"))
#     print(i.group("ren"))

"""6.豆瓣Top250"""
# import requests
# import re
# import csv
#
# page_content=''
# for n in range(0,250,25):
#     url=f"https://movie.douban.com/top250?start={n}&filter="
#     head={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3868.400 QQBrowser/10.8.4394.400"}
#     resp=requests.get(url, headers=head)
#     page_content+=resp.text  # 页面源代码
# obj=re.compile(r'<li>.*?<div class="item">.*?<span class="title">(?P<name>.*?)'
#                r'</span>.*?<p class="">.*?<br>(?P<year>.*?)&nbsp.*?'
#                r'<span class="rating_num" property="v:average">(?P<score>.*?)</span>.*?'
#                r'<span>(?P<num>.*?)</span>', re.S)  # 解析数据
# res=obj.finditer(page_content)
# # for it in res:
# #     print(it.group("name"), end="\t")
# #     print(it.group("year").strip(), end="\t")
# #     print(it.group("score"), end="\t")
# #     print(it.group("num"))
# with open("data.csv", mode='w', encoding='utf-8') as f:
#     csvw=csv.writer(f)
#     for it in res:
#         dic=it.groupdict()
#         dic['year']=dic['year'].strip()
#         csvw.writerow(dic.values())
# print('over!')

"""7.电影天堂"""
# import requests
# import re
# import csv
#
# domain='https://dytt89.com/'
# resp=requests.get(domain, verify=False)  # 去掉安全验证
# resp.encoding='gb2312'  # 指定字符集
# page_content=resp.text  # 页面源代码
# obj1=re.compile(r'2021必看热片.*?<ul>(?P<ul>.*?)</ul>', re.S)
# obj2=re.compile(r"<a href='(?P<href>.*?)'", re.S)
# obj3=re.compile(r'◎片　　名(?P<movie>.*?)<br />.*?<td style="WORD-WRAP: '
#                 r'break-word" bgcolor="#fdfddf"><a href="(?P<download>.*?)">', re.S)
# res1=obj1.finditer(page_content)
# child_href_list=[]
# for it in res1:
#     # print(it.group("ul"), end="\t")
#     ul=it.group("ul")
#     res2=obj2.finditer(ul)
#     for it in res2:
#         child_href=domain + it.group("href").strip('/')   # 子网站域名需要拼接
#         # print(child_href)
#         child_href_list.append(child_href)
# for href in child_href_list:
#     child_resp=requests.get(href, verify=False)
#     child_resp.encoding='gb2312'
#     child_page_content=child_resp.text
#     # print(child_page_content)
#     # break
#     # res3=obj3.finditer(child_page_content)
#     # for it in res3:
#     #     print(it.group("movie"), end="\t")
#     #     print(it.group("download"))
#     res3 = obj3.search(child_page_content)
#     print(res3.group("movie"), end="\t")
#     print(res3.group("download"))
#     # break

"""8.bs4解析（HTML语法）"""
# import requests
# from bs4 import BeautifulSoup
# import csv
#
# f=open("data.csv", mode='w', encoding='utf-8')
# csvw=csv.writer(f)
#
# url="http://www.xinfadi.com.cn/marketanalysis/0/list/1.shtml"
# resp=requests.get(url)
# # print(resp.text)
# page=BeautifulSoup(resp.text, "html.parser")  # 指定HTML解析器
# # table=page.find("table", class_="hq_table")  # class是python中的关键字，用class_即可
# table=page.find("table", attrs={"class": "hq_table"})  # 用字典也行，可避免class关键字冲突
# # print(table)
# trs=table.find_all("tr")[1:]
# for tr in trs:
#     tds=tr.find_all("td")
#     name=tds[0].text
#     low = tds[1].text
#     avg = tds[2].text
#     high = tds[3].text
#     gui = tds[4].text
#     kind = tds[5].text
#     date = tds[6].text
#     csvw.writerow([name, low, avg, high, gui, kind, date])
# f.close()
# print('over!')

"""9.优美图库"""
# import requests
# from bs4 import BeautifulSoup
# import time
#
# url="https://www.umei.net/bizhitupian/weimeibizhi/"
# resp=requests.get(url)
# resp.encoding='utf-8'  # 指定字符集
# # print(resp.text)
# main_page=BeautifulSoup(resp.text, "html.parser")  # 指定HTML解析器
# alist=main_page.find("div", class_="TypeList").find_all("a")
# # print(alist)
# for a in alist:
#     # print('https://www.umei.net/'+a.get('href'))  # 直接通过get就可以拿到属性值
#     # 获取子页面源代码
#     href='https://www.umei.net/'+a.get('href')
#     child_resp = requests.get(href)
#     child_resp.encoding = 'utf-8'  # 指定字符集
#     # print(child_resp.text)
#     # break
#     # 从子页面中拿下载路径
#     child_page = BeautifulSoup(child_resp.text, "html.parser")  # 指定HTML解析器
#     img = child_page.find("div", class_="ImageBody").find('img')
#     src = img.get('src')
#     # 下载图片
#     img_resp = requests.get(src)
#     # img_resp.content  # 这里拿到的是字节
#     img_name = src.split('/')[-1]  # 拿到URL中最后一个/后的内容
#     with open('img/'+img_name, mode='wb') as f:
#         f.write(img_resp.content)  # 图片内容写入文件
#     print(img_name, 'download over!')
#     time.sleep(1)  # 为了防止大量请求被服务器识别后被干掉
# print('all over!!')

"""10.xpath解析"""
# # xpath 是XML文档中搜索内容的一门语言
# # HTML 是XML的一个子集
# from lxml import etree
#
# xml = """
# <note>
#     <to>Tove</to>
#     <nick>Jani</nick>
#     <author>
#         <nick id="111">安抚</nick>
#         <nick id="222">阿道夫</nick>
#         <div>
#             <nick id="333">所覆盖1</nick>
#         </div>
#         <div>
#             <nick id="444">所覆盖2</nick>
#             <span>
#                 <nick id="555">所覆盖3</nick>
#             </span>
#         </div>
#     </author>
#     <body>Don't forget me this weekend!</body>
# </note>
# """
# tree = etree.XML(xml)
# # res = tree.xpath('/note')
# # res = tree.xpath('/note/author')
# # res = tree.xpath('/note/author/nick/text()')  # text()是拿文本
# # res = tree.xpath('/note/author//nick/text()')  # 后代全取出来
# # res = tree.xpath('/note/author/*/nick/text()')  # *表示任意节点，即通配符
# res = tree.xpath('/note//nick/text()')
# print(res)

"""11.xpath解析"""
# from lxml import etree
#
# tree = etree.parse("b.html")
# # res = tree.xpath('/html')
# # res = tree.xpath('/html/body/ul/li/a/text()')
# # res = tree.xpath('/html/body/ul/li[1]/a/text()')  # xpath的顺序是从1开始数的
# # res = tree.xpath('/html/body/ol/li/a[@href="dapao"]/text()')  # [@xx=xxx] 属性筛选
# # print(res)
#
# # ol_li_list = tree.xpath('/html/body/ol/li')
# # for li in ol_li_list:
# #     res = li.xpath('./a/text()')  # 在li中继续查找，是相对查找
# #     print(res)
# #     res2 = li.xpath('./a/@href')  # @属性  可以拿到属性值
# #     print(res2)
#
# # print(tree.xpath('/html/body/ul/li/a/@href'))
# print(tree.xpath('/html/body/div[1]/text()'))

"""12.猪八戒网"""
# import requests
# from lxml import etree
#
# url = "https://xian.zbj.com/search/f/?type=new&kw=saas"
# resp = requests.get(url)
# # print(resp.text)
# # 解析
# html = etree.HTML(resp.text)
# # 拿到每一个服务商的div
# divs = html.xpath('/html/body/div[6]/div/div/div[2]/div[6]/div[1]/div')
# # 遍历每一个服务商的div
# for div in divs:
#     # price = div.xpath('./div/div/a[1]/div[2]/div[1]/span[1]/text()')
#     # title = div.xpath('./div/div/a[1]/div[2]/div[2]/p/text()')
#     # company = div.xpath('./div/div/a[2]/div[1]/p/text()')
#     # location = div.xpath('./div/div/a[2]/div[1]/div/span/text()')
#     # print(price)
#     # print(title)
#     # print(company)
#     # print(location)
#
#     price = div.xpath('./div/div/a[1]/div[2]/div[1]/span[1]/text()')[0].strip('¥')
#     title = 'saas'.join(div.xpath('./div/div/a[1]/div[2]/div[2]/p/text()'))
#     company = div.xpath('./div/div/a[2]/div[1]/p/text()')[0]
#     location = div.xpath('./div/div/a[2]/div[1]/div/span/text()')[0]
#     print(price)
#     print(title)
#     print(company)
#     print(location)

"""request进阶"""
"""13.模拟用户登录（cookie）"""
# # 登录->得到cookie
# # 带着cookie去请求到书架ur1->书架上的内容
# # 必须得把上面的两个操作连起来
# # 我们可以使用session进行请求->session可以被认为是一连串的请求。在这个过程中的cookie不会丢失
# import requests
#
# # 会话
# session = requests.session()
# data = {
#     "loginName": "188****8295",
#     "password": "188****8295wdzh"
# }
# # 登录
# url = "https://passport.17k.com/ck/user/login"
# # resp = session.post(url, data=data)
# session.post(url, data=data)
# # print(resp.text)
# # print(resp.cookies)
# # 获取书架内容
# c_url = "https://user.17k.com/ck/author/shelf?page=1&appKey=2406394919"
# c_resp = session.get(c_url)
# # print(c_resp.text)
# print(c_resp.json())
#
# # 以上为第一种方案，通过session的方式隐藏Cookie的方式，拿到数据
#
# # 第二种方案，直接复制Cookie，暴力拿到数据
# # 直接用Cookie也是可以的
# # c_url = "https://user.17k.com/ck/author/shelf?page=1&appKey=2406394919"
# # c_resp = requests.get(c_url, headers={"Cookie": "GUID=2354c790-2f67-4b10-8f3e-1b6399d23bac; sajssdk_2015_cross_new_user=1; c_channel=0; c_csc=web; Hm_lvt_9793f42b498361373512340937deb2a0=1621306180,1621306332; accessToken=avatarUrl%3Dhttps%253A%252F%252Fcdn.static.17k.com%252Fuser%252Favatar%252F09%252F49%252F86%252F77118649.jpg-88x88%253Fv%253D1621307467000%26id%3D77118649%26nickname%3D626wdzh%26e%3D1636859844%26s%3D52c8226defd152f0; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2277118649%22%2C%22%24device_id%22%3A%221797d610048ee-02df88b0e4f46c-33524a72-2073600-1797d61004b22%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%A4%BE%E4%BA%A4%E7%BD%91%E7%AB%99%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22https%3A%2F%2Fapi.weibo.com%2Foauth2%2Fauthorize%3Fclient_id%3D1115774813%26redirect_uri%3Dhttps%253A%252F%252Fpassport.17k.com%252Fsns%252FweiBoCallback.action%253FfromUrl%253Dhttps%25253A%25252F%25252Fuser.17k.com%25252Fwww%25252Fbookshelf%25%22%2C%22%24latest_referrer_host%22%3A%22api.weibo.com%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC%22%7D%2C%22first_id%22%3A%222354c790-2f67-4b10-8f3e-1b6399d23bac%22%7D; Hm_lpvt_9793f42b498361373512340937deb2a0=1621308287"})
# # print(c_resp.json())

"""14.防盗链（处理反扒，抓取视频）"""
# import requests
#
# "https://www.pearvideo.com/video_1728773"
# "https://video.pearvideo.com/mp4/third/20210507/cont-1728773-12086796-144020-hd.mp4"
# "https://video.pearvideo.com/mp4/third/20210507/1621310013052-12086796-144020-hd.mp4"
# # 1.拿到contId
# url = "https://www.pearvideo.com/video_1728773"
# contId = url.split("_")[1]
# videoStatusUrl = f"https://www.pearvideo.com/videoStatus.jsp?contId={contId}&mrd=0.4971280371577558"
# # 2.拿到videoStatus返回的json.->SrCURL
# headers = {
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3868.400 QQBrowser/10.8.4394.400",
#     # 防盗链：溯源，当前请求的上一级
#     # "Referer": "https://www.pearvideo.com/video_1728773"
#     "Referer": url
# }
# resp = requests.get(videoStatusUrl, headers = headers)
# # print(resp.json())
# dic = resp.json()
# srcUrl = dic['videoInfo']['videos']['srcUrl']
# # print(srcUrl)
# # 3.srCURL里面的内容进行修整
# systemTime = dic['systemTime']
# # print(systemTime)
# srcUrl = srcUrl.replace(systemTime, f"cont-{contId}")
# # print(srcUrl)
# # 4.下载视频(下载视频和下载图片是一样的，都是下载文件)
# with open('video/a.mp4', mode="wb") as f:
#     f.write(requests.get(srcUrl).content)

"""15.代理"""
# 原理：通过第三方的机器去发送请求
import requests

proxies = {
    # "http": "",
    # "https": "139.9.25.69:3128"
    "https": "https://139.9.25.69:3128"
}
resp = requests.get("https://www.baidu.com", proxies=proxies)
resp.encoding = "utf-8"
print(resp.text)




"""综合训练：抓取网易云音乐评论信息"""


