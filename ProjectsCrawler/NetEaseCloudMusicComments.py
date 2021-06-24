# @License : 西安工业大学
# @Author  : 王泽 WZ-Dale
# @Time    : 2021/5/19 9:48

"""综合训练：抓取网易云音乐评论信息"""
# 1.找到未加密的参数        # windows.asrsea(参数, xxxxx, xxxxx)
# 2.想办法把参数进行加密（必须参考网易的逻辑），params => encText，encSeckey => encSeckey
# 3.请求到网易，拿到评论信息

import requests
import json
from Crypto.Cipher import AES
from base64 import b64encode

url = "https://music.163.com/weapi/comment/resource/comments/get?csrf_token="
data = {
    "csrf_token": "",
    "cursor": "-1",
    "offset": "0",
    "orderType": "1",
    "pageNo": "1",
    "pageSize": "20",
    "rid": "R_SO_4_1325905146",
    "threadId": "R_SO_4_1325905146"
}
e = "010001"
f = "00e0b509f6259df8642dbc35662901477df22677ec152b5ff68ace615bb7b725152b3ab17a876aea8a5aa76d2e417629ec4ee341f56135fccf695280104e0312ecbda92557c93870114af6c9d05c4f7f0c3685b7a46bee255932575cce10b424d813cfe4875d3e82047b97ddef52741d546b8e289dc6935b3ece0462db0a22b8e7"
g = "0CoJUm6Qyw8W8jud"
i = "UPtGlrQKqFK4SXZn"

def get_encSeckey():
    return "9878240d74b866d33bd080af706cf28d7244a9993c02325fe3570165c7a59a31435cc0475618bed2f7f428a0a2961316ac0e45c9e83ccc4385c439e30984d02f7d9319129bb0ea2b06957096aa9fa6a9ffa907ad8016cfed88105c75699459923a9b4bd313915a69bf5da0bfb115751af6e0032c9741612fb66322cda13c3344"

def get_params(data):
    first = enc_params(data, g)
    second = enc_params(first, i)
    return second

def to_16(data):
    pad = 16 - len(data) % 16
    data += chr(pad) * pad
    return data

def enc_params(data, key):  # 加密过程
    iv = "0102030405060708"
    data = to_16(data)
    aes = AES.new(key=key.encode("utf-8"), IV=iv.encode("utf-8"), mode=AES.MODE_CBC)
    bs = aes.encrypt(data.encode("utf-8"))  # 加密加密的内容必须是16的倍数
    return str(b64encode(bs), "utf-8")      # 转化为字符串并返回

# 处理加密过程
"""
    function a(a) {     # a = 16
        var d, e, b = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789", c = "";
        for (d = 0; a > d; d += 1)      # 循环16次
            e = Math.random() * b.length,       # 产生随机数
            e = Math.floor(e),          # 取整
            c += b.charAt(e);           # 取出字符串中位置为e的字符
        return c                # 返回随机的16位字符串
    }
    function b(a, b) {
        var c = CryptoJS.enc.Utf8.parse(b)
          , d = CryptoJS.enc.Utf8.parse("0102030405060708")
          , e = CryptoJS.enc.Utf8.parse(a)
          , f = CryptoJS.AES.encrypt(e, c, {
            iv: d,
            mode: CryptoJS.mode.CBC
        });
        return f.toString()
    }
    function c(a, b, c) {
        var d, e;
        return setMaxDigits(131),
        d = new RSAKeyPair(b,"",c),
        e = encryptedString(d, a)
    }
    function d(d, e, f, g) {    # d: 数据   e: 定值 "010001"   f: 很长     g: "0CoJUm6Qyw8W8jud"
        var h = {}              # 空对象
          , i = a(16);          # 16位随机字符串
        return h.encText = b(d, g),
        h.encText = b(h.encText, i),    # 得到params
        h.encSecKey = c(i, e, f),       # 得到encSeckey，e和f是定值
        h
    }
"""

resp = requests.post(url, data={
    "params": get_params(json.dumps(data)),
    "encSecKey": get_encSeckey()
})
print(resp.text)
