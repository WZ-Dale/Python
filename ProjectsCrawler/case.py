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
#     "loginName": "1********",
#     "password": "1********8295wdzh"
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
# # 原理：通过第三方的机器去发送请求
# import requests
#
# proxies = {
#     # "http": "",
#     # "https": "139.9.25.69:3128"
#     "https": "https://139.9.25.69:3128"
# }
# resp = requests.get("https://www.baidu.com", proxies=proxies)
# resp.encoding = "utf-8"
# print(resp.text)



"""16.多线程"""

from threading import Thread

"""第一种写法，小脚本"""
# def fun():
#     for i in range(1000):
#         print("fun()", i)
# if __name__ == '__main__':
#     t = Thread(target=fun)        # 创建线程并给线程安排任务
#     t.start()                     # 多线程状态为可开始工作状态，具体的执行时间由CPU决定
#     for i in range(1000, 2000):
#         print("main()", i)

"""第二种写法，业内大佬"""
# class MyThread(Thread):
#     def run(self):  # 当线程被执行的时候，被执行的就是这个run()
#         for i in range(1000):
#             print("子线程中 ", i)
# if __name__ == '__main__':
#     t = MyThread()
#     # t.run()       # 方法的调用，还是单线程
#     t.start()       # 开启线程
#     for i in range(1000, 2000):
#          print("主线程中 ", i)

"""17.多进程"""
"""开进程太费劲了"""
from multiprocessing import Process

"""第一种写法"""
# def fun():
#     for i in range(1000):
#         print("fun()", i)
# if __name__ == '__main__':
#     p = Process(target=fun)
#     p.start()
#     for i in range(1000, 2000):
#         print("main()", i)

"""第二种写法"""
# class MyProcess(Process):
#     def run(self):
#         for i in range(1000):
#             print("子进程中 ", i)
# if __name__ == '__main__':
#     p = MyProcess()
#     p.start()
#     for i in range(1000, 2000):
#          print("主进程中 ", i)

"""18.线程传参"""
# def fun(name):
#     for i in range(1000):
#         print(name, i)
# if __name__ == '__main__':
#     t1 = Thread(target=fun, args=("线程1 ",))     # 传递参数必须是元组，注意加逗号
#     t1.start()
#     t2 = Thread(target=fun, args=("线程2 ",))
#     t2.start()
#     for i in range(1000, 2000):
#         print("主线程 ", i)

"""19.进程池和线程池"""
# # 线程池：一次性开辟一批线程，用户直接给线程池提交任务，线程任务的调度交给交给线程池来完成
# from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
#
# def fn(name):
#     for i in range(100):
#         print(name, i)
#
# if __name__ == '__main__':
#     with ThreadPoolExecutor(50) as t:       # 创建线程池，进程池使用ProcessPoolExecutor
#         for i in range(100):
#             t.submit(fn, name=f"线程{i}")   # 将任务提交给线程池
#     # 等待线程池中的任务全部执行完毕，才继续执行（守护）
#     print("over!!")

"""20.使用线程池爬取北京新发地"""
# import requests
# from lxml import etree
# import csv
# from concurrent.futures import ThreadPoolExecutor
#
# f = open("BeiingXinfadi.csv", mode='w', newline='', encoding='utf-8')
# csvw = csv.writer(f)
#
# def download_one_page(url):
#     resp = requests.get(url)
#     html = etree.HTML(resp.text)
#     table = html.xpath("/html/body/div[2]/div[4]/div[1]/table")[0]
#     # trs = table.xpath("./tr")[1:]
#     trs = table.xpath("./tr[position()>1]")
#     for tr in trs:
#         txt = tr.xpath("./td/text()")
#         # 对数据做简单处理：去掉\\和/
#         txt = (item.replace("\\", "").replace("/", "") for item in txt)
#         csvw.writerow(txt)
#     print(url, "提取完毕！")
#
# if __name__ == '__main__':
#     # 单线程，效率低下
#     # for i in range(1, 89):
#     #     url = f"http://www.xinfadi.com.cn/marketanalysis/0/list/{i}.shtml"
#     #     download_one_page(url)
#     # 多线程和线程池
#     with ThreadPoolExecutor(50) as t:
#         for i in range(1, 89):
#             url = f"http://www.xinfadi.com.cn/marketanalysis/0/list/{i}.shtml"
#             t.submit(download_one_page, url=url)
#     print("over!!")

"""21.协程"""
# 当程序处于IO操作的时候，线程就会处于阻塞状态（输入，网络请求）
# 协程：当程序遇见IO操作的时候，可以选择性的切换到其他任务上，高效利用CPU
# 微观上，是一个任务一个任务的进行切换，切换条件一般就是IO操作
# 宏观上，我们看到的是多个任务一起执行
# 多任务异步操作
# 上方所描述的一切都是在单线程的条件下
import asyncio
import time

# async def fun():    # 此时的函数是异步协程函数，函数执行得到的是一个协程对象
#     print("Outstanding!")
#
# if __name__ == '__main__':
#     g = fun()
#     # print(g)
#     asyncio.run(g)  # 协程程序的运行需要asyncio模块的支持

# async def fun1():
#     print("Outstanding!")
#     # time.sleep(2)       # 当程序中出现了同步操作的时候，异步就中断了
#     await asyncio.sleep(2)    # 异步操作的代码
#     print("Excellent")
# async def fun2():
#     print("Common!")
#     # time.sleep(3)
#     await asyncio.sleep(3)
#     print("General")
# async def fun3():
#     print("Weak!")
#     # time.sleep(4)
#     await asyncio.sleep(4)
#     print("Short")
#
# if __name__ == '__main__':
#     f1 = fun1()
#     f2 = fun2()
#     f3 = fun3()
#     tasks = [f1, f2, f3]
#     t1 = time.time()
#     # 一次性启动多个任务（协程）
#     asyncio.run(asyncio.wait(tasks))
#     t2 = time.time()
#     print(t2 - t1)

"""协程的几种写法"""
# async def fun1():
#     print("Outstanding!")
#     await asyncio.sleep(2)
#     print("Excellent")
# async def fun2():
#     print("Common!")
#     await asyncio.sleep(3)
#     print("General")
# async def fun3():
#     print("Weak!")
#     await asyncio.sleep(4)
#     print("Short")
#
# async def main():
#     # 第一种写法
#     # f1 = fun1()
#     # await f1    # 一般await挂起操作放在协程对象前面
#     # 第二种写法（推荐）
#     tasks = [
#         asyncio.create_task(fun1()),  # 在python3.8之后用这种方法 asyncio.create_task()
#         asyncio.create_task(fun2()),
#         asyncio.create_task(fun3())
#     ]
#     await asyncio.wait(tasks)
#
# if __name__ == '__main__':
#     t1 = time.time()
#     asyncio.run(main())
#     t2 = time.time()
#     print(t2 - t1)

"""例举一个爬虫，使用协程"""
# async def download(url):
#     print("开始下载")
#     await asyncio.sleep(3)      # 网络请求
#     print("下载完成")
#
# async def main():
#     urls = {
#         "http://www.baidu.com",
#         "http://www.bilibili.com",
#         "http://www.163.com"
#     }
#     tasks = []
#     for url in urls:
#         d = download(url)
#         tasks.append(asyncio.create_task(d))
#     await asyncio.wait(tasks)
#
# if __name__ == '__main__':
#     asyncio.run(main())

"""22.异步http请求aiohttp模块"""
# # requests.get()是同步的代码，异步操作要用aiohttp
# import asyncio
# import aiohttp
#
# urls = [
#     "http://kr.shanghai-jiuxin.com/file/2020/1031/d7de3f9faf1e0ecdea27b73139fc8d3a.jpg",
#     "http://kr.shanghai-jiuxin.com/file/2020/1031/191468637cab2f0206f7d1d9b175ac81.jpg",
#     "http://kr.shanghai-jiuxin.com/file/2020/1031/a2c58d6d726fb7ef29390becac5d8643.jpg"
# ]
#
# async def aiodownload(url):
#     # 异步的 s = aiohttp.ClientSession() 等同于同步的 request
#     # request.get()     request.post()
#     # s.get()           s.post()
#     name = url.rsplit("/", 1)[1]
#     async with aiohttp.ClientSession() as session:
#         # 发送请求
#         async with session.get(url) as resp:
#             # resp.content.read()     # 等价于之前的resp.content
#             # resp.text()             # 等价于之前的resp.test
#             # resp.json()  # 等价于之前的resp.ison()
#             # 保存文件，可以自学一个模块aiofiles
#             with open("img1/"+name, mode ="wb") as f:
#                 f.write(await resp.content.read())  # 得加await挂起，异步读取（什么时候有内容了，什么时候才读取）
#     print(name, "搞定")
#
# async def main():
#     tasks = []
#     for url in urls:
#         d = aiodownload(url)
#         tasks.append(asyncio.create_task(d))
#     await asyncio.wait(tasks)
#
# if __name__ == '__main__':
#     asyncio.run(main())

"""23.用协程扒光一部小说"""
# ## url="https://dushu.baidu.com/pc/detail?gid=4306063500"
# ## url1='https://dushu.baidu.com/api/pc/getCatalog?data={"book_id":"4306063500"}'   # 所有章节的名称、cid
# ## url2='https://dushu.baidu.com/api/pc/getChapterContent?data={"book_id":"4306063500","cid":"4306063500|11348571","need_bookinfo":1}'     # 章节内容
#
# # 1.同步操作：访问getCatalog，从而拿到所有章节的名称和cid
# # 2.异步操作：访问getChapterContent，从而下载章节内容
#
# import requests
# import asyncio
# import aiohttp
# import json
# import aiofiles
#
# async def aiodownload(b_id, cid, title):
#     data = {
#         "book_id": b_id,
#         "cid": f"{b_id}|{cid}",
#         "need_bookinfo": 1
#     }
#     data = json.dumps(data)
#     url = f'https://dushu.baidu.com/api/pc/getChapterContent?data={data}'
#     async with aiohttp.ClientSession() as session:
#         async with session.get(url) as resp:
#             dic = await resp.json()
#             async with aiofiles.open("Xiyouji/"+title+".txt", mode ="w", encoding='utf-8') as f:
#                 await f.write(dic['data']['novel']['content'])
#     print(title, "搞定")
#
# async def getCatalog(url):
#     resp = requests.get(url)
#     dict = resp.json()
#     tasks = []
#     for item in dict['data']['novel']['items']:
#         title = item['title']
#         cid = item['cid']
#         # 准备异步任务
#         d = aiodownload(b_id, cid, title)
#         tasks.append(asyncio.create_task(d))
#     await asyncio.wait(tasks)
#
# if __name__ == '__main__':
#     b_id = "4306063500"
#     url = 'https://dushu.baidu.com/api/pc/getCatalog?data={"book_id":"'+ b_id +'"}'
#     asyncio.run(getCatalog(url))


# 需求：能不能让程序连接到浏览器，让浏览器来完成各种复杂的操作，我们只接受最终的结果
"""24.selenium引入概念"""
# # selenium刚开始只是自动化测试工具
# # selenium可以打开浏览器，然后像人一样去操作浏览器
# # 程序员可以直接从selenium中提取网页上的各种信息
# # 环境搭建：pip install selenium -i 清华源
# #           下载浏览器驱动：http://npm.taobao.org/mirrors/chromedriver
# #           把解压缩的浏览器驱动 chromedriver 放在python解释器所在文件夹中
#
# from selenium.webdriver import Chrome
#
# # 1.创建浏览器对象
# web = Chrome()
# # 2.打开网址
# web.get("http://www.baidu.com")
# # web.close()
# print(web.title)

"""25.抓取拉钩网站"""
# from selenium.webdriver import Chrome
# from selenium.webdriver.common.keys import Keys
# import time
#
# web = Chrome()
# web.get("http://lagou.com")
# # 找到某个元素，点击它
# el = web.find_element_by_xpath('//*[@id="changeCityBox"]/p[1]/a')
# el.click()      # 点击事件
# time.sleep(1)   # 让浏览器缓一会
# # 找到输入框，输入内容，再点回车或者点击搜索框按钮
# web.find_element_by_xpath('//*[@id="search_input"]').send_keys("C++服务器开发", Keys.ENTER)
# # 查找存放数据的位置，进行数据提取
# # 找到页面中存放数据的所有的li
# li_list = web.find_elements_by_xpath('//*[@id="s_position_list"]/ul/li')
# time.sleep(1)
# for li in li_list[1:]:
#     job_name = li.find_element_by_tag_name("h3").text           # 通过标签找
#     company_name = li.find_element_by_xpath('./div/div[2]/div/a').text
#     job_price = li.find_element_by_xpath('./div/div/div[2]/div/span').text      # 通过路径找
#     print(job_name, company_name, job_price)

# selenium 的优点：1.所见即所得；2.简单
# selenium 的软肋：1.加载速度慢；2.反扒
"""26.窗口之间的切换"""
# from selenium.webdriver import Chrome
# from selenium.webdriver.common.keys import Keys
# import time
"""第一种切换方式"""
# web = Chrome()
# web.get("http://lagou.com")
# el = web.find_element_by_xpath('//*[@id="cboxClose"]').click()
# time.sleep(1)
# web.find_element_by_xpath('//*[@id="search_input"]').send_keys("C++服务器开发", Keys.ENTER)
# time.sleep(1)
# web.find_element_by_xpath('//*[@id="s_position_list"]/ul/li[2]/div[1]/div[1]/div[1]/a/h3').click()
# # 注意：在selenium的眼中，自己还在旧窗口中，并没有切换到新窗口中
# # 进行窗口切换：
# web.switch_to.window(web.window_handles[-1])    # 切换到最后一个窗口
# # 在新窗口进行信息提取：
# job_detail = web.find_element_by_xpath('//*[@id="job_detail"]/dd[2]/div').text
# print(job_detail)
# # 关掉当前子窗口
# web.close()
# # 切换selenium的窗口视角，回到原来的窗口中
# web.switch_to.window(web.window_handles[0])
# # 测试是否跳转回来了
# print(web.find_element_by_xpath('//*[@id="s_position_list"]/ul/li[2]/div[1]/div[1]/div[1]/a/h3').text)
"""第二种切换方式"""
# web = Chrome()
# # 如果页面中遇到了iframe如何处理：
# web.get('https://91kanju.com/vod-play/541-2-1.html')
# # 处理iframe的话，必须先拿到iframe，然后切换视角到iframe，然后才可以拿到数据
# iframe = web.find_element_by_xpath('//*[@id="player_iframe"]')
# web.switch_to.frame(iframe)
# # web.switch_to.default_content()     # 切换到默认窗口（即切换回原页面）
# tx =web.find_element_by_xpath('//*[@id="sub-frame-error"]').text
# print(tx)

"""27.无头浏览器"""
# from selenium.webdriver import Chrome
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.support.select import Select
# import time
#
# # 准备好参数配置
# opt = Options()
# opt.add_argument('--headless')      # 无头
# opt.add_argument('--disable-gpu')   # 显卡不可用
#
# web = Chrome(options=opt)   # 把参数配置设置到浏览器中
# web.get('https://www.endata.com.cn/BoxOffice/Bo/Year/index.html')
# # 定位到下拉列表
# sel_el = web.find_element_by_xpath('//*[@id="OptionDate"]')
# # 对元素进行包装，包装成下拉菜单
# sel = Select(sel_el)
# # 让浏览器进行调整选项
# for i in range(len(sel.options)):   # i即是下拉框选项的索引位置
#     sel.select_by_index(i)          # 按照索引进行切换
#     time.sleep(2)
#     table = web.find_element_by_xpath('//*[@id="TableList"]/table')
#     print(table.text)
#     print('======================================================')
# print("运行完毕！")
# web.close()
#
# # 如何拿到页面代码Elements（经过数据加载以及js执行之后的结果的html内容）（并不是页面源代码，而是动态加载的html）
# # print(web.page_source)

"""28.验证码（用超级鹰干超级鹰）"""
# # 1.图像识别
# # 2.选择互联网上成熟的验证码破解工具
# # 推荐使用“超级鹰”
# from selenium.webdriver import Chrome
# from chaojiying import Chaojiying_Client
# import time
#
# web = Chrome()
# web.get('http://www.chaojiying.com/user/login/')
# # 处理验证码
# img = web.find_element_by_xpath('/html/body/div[3]/div/div[3]/div[1]/form/div/img').screenshot_as_png
# chaojiying = Chaojiying_Client('账号', '密码', '软件ID')
# dic = chaojiying.PostPic(img, 1902)
# verify_code = dic['pic_str']
# # 填账号、密码、验证码
# web.find_element_by_xpath('/html/body/div[3]/div/div[3]/div[1]/form/p[1]/input').send_keys('账号')
# web.find_element_by_xpath('/html/body/div[3]/div/div[3]/div[1]/form/p[2]/input').send_keys('密码')
# web.find_element_by_xpath('/html/body/div[3]/div/div[3]/div[1]/form/p[3]/input').send_keys(verify_code)
# time.sleep(5)
# # 点击登录
# web.find_element_by_xpath('/html/body/div[3]/div/div[3]/div[1]/form/p[4]/input').click()

