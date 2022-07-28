# -*- coding: utf-8 -*-
# @Author  : 夏洛
# @File    : xialuo.py
# @VX : tl210329

import pprint

import copyheaders
import execjs
from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.triggers.interval import IntervalTrigger
import time
from configparser import ConfigParser
import requests
import json

recent = {
    "newsid": ''
}

headers = copyheaders.headers_raw_to_dict(b"""
accept: application/json, text/plain, */*
content-type: application/json;charset=UTF-8
origin: https://xhpfmapi.zhongguowangshi.com
referer: https://xhpfmapi.zhongguowangshi.com/vh512/account/25295
user-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.80 Safari/537.36 Edg/98.0.1108.50
""")

code_js = """
    const CryptoJS = require('crypto-js')
    function des_decrypt(str)
    {
        var key			= CryptoJS.MD5('Xinhuamm@2018').toString();
        var crypto_key 	= CryptoJS.enc.Utf8.parse(key);
        var decrypt_str	= CryptoJS.TripleDES.decrypt(str, crypto_key, {
                            mode: 		CryptoJS.mode.ECB,
                            padding: 	CryptoJS.pad.Pkcs7});
        return 	decrypt_str.toString(CryptoJS.enc.Utf8);
    }
    function enc_crypt(pagenum)
    {
        var str = '{"cid":"25295","pn":'+pagenum.toString()+',"clientVer":"8.8.2","clientLable":"h5","source":0,"userID":""}'
        var key			= CryptoJS.MD5('Xinhuamm@2018').toString();
        var crypto_key 	= CryptoJS.enc.Utf8.parse(key);
        var decrypt_str	= CryptoJS.TripleDES.encrypt(str, crypto_key, {
                            mode: 		CryptoJS.mode.ECB,
                            padding: 	CryptoJS.pad.Pkcs7});
        console.log(decrypt_str.ciphertext)
        return 	CryptoJS.enc.Base64.stringify(decrypt_str.ciphertext);
    }
"""


class Config(object):
    '''解析配置文件'''

    def get_config(self, lable, value):
        cf = ConfigParser()
        cf.read("./config/CONFIG.conf")
        config_value = cf.get(lable, value)
        return config_value


def enc_func(data):
    datac = execjs.compile(code_js)
    encdata = datac.call("des_decrypt", data)
    return encdata


def getparams(currentpage):
    datac = execjs.compile(code_js)
    encdata = datac.call("enc_crypt", currentpage)
    print(f"获取请求参数：{encdata}")
    return encdata


def dowork():
    print(f'\n正在执行任务：{time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())}')
    current_con = []
    base_api = 'https://xhpfmapi.zhongguowangshi.com/v600/core/columnnewslist'
    res = requests.post(
        base_api,
        headers=headers,
        data='{"param":"' + getparams(currentpage=1) + '"}'
    )
    re_data = json.loads(enc_func(res.json().get("data"))).get("newsList")[:3]
    print(f"当前列表新闻：{len(re_data)}")
    for item in re_data:
        saveitem = {}
        saveitem["newsid"] = item.get("id")
        saveitem["title"] = item.get("topic")
        saveitem["time"] = time.strftime('%Y-%m-%d %H:%M')
        saveitem["url"] = item.get("detailurl")
        saveitem["fulltext"] = get_full(item.get("id"))
        current_con.append(saveitem)
        print('数据预览', saveitem.get("newsid"), saveitem.get("time"), saveitem.get("title"),
              saveitem.get("fulltext")[4080:4100])

    ###过滤出新数据
    filter_news = []
    for inew in current_con:
        if str(inew.get("newsid")) == str(recent.get("newsid")):
            break
        filter_news.append(inew)
    print(f"当前程序跑出新数据：{len(filter_news)}")

    ###更新最新id
    recent["newsid"] = re_data[0].get("id")

    ###过滤出含有指定关键字的数据
    contains_kw_list = []
    with open("./config/keyword.txt", 'r', encoding='utf-8') as fc:
        keys = [i.strip() for i in fc.readlines()]
    print(f'keyword列表：{keys}')
    for inw in filter_news:
        for ik in keys:
            if ik in inw.get("fulltext"):
                inw['containskw'] = ik
                contains_kw_list.append(inw)
                break

    ###f发送消息到微信客户端
    print(f"含有指定关键字新闻条数：{len(contains_kw_list)}")
    for ickl in contains_kw_list:
        sendinfo(ickl)


def sendinfo(obj):
    title = obj.get("title")
    time = obj.get("time")
    url = obj.get("url")
    containskw = obj.get("containskw")
    html = """
    标题： %s
    时间：%s
    链接： %s
    关键字: %s
    """ % (title, time, url, containskw)
    print('\n' + '*' * 50)
    print(f"title: {title}")
    print(f"time: {time}")
    print(f"containskw: {containskw}")
    print(f"url: {url}")
    print('*' * 50)
    cfg = Config()
    wx_key = cfg.get_config("mass", "KEY")
    wx_webhookurl = 'https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key={}'.format(wx_key)
    headers = {'Content-Type': 'application/json'}
    hbpeople = ["san.zhang"]
    msg = html
    testdata = json.dumps({"msgtype": "text", "text": {"content": msg, "mentioned_list": hbpeople}})
    r = requests.post(wx_webhookurl, data=testdata, headers=headers, verify=False)
    print(r.text)


def get_full(pid):
    url = f'https://xhpfmapi.xinhuaxmt.com/v600/news/{pid}.js?ts=0&share=1'
    res = requests.get(url, headers=headers)
    return res.text


if __name__ == "__main__":
    dowork()
    ####创建时间调度器，每隔60分钟执行一次
    trigger_interval = IntervalTrigger(seconds=60, timezone='Asia/Shanghai')
    ##创建任务调度器
    scheduler = BlockingScheduler(timezone='Asia/Shanghai')
    ##添加时间间隔任务
    scheduler.add_job(dowork, trigger=trigger_interval, seconds=60)
    ###开始调度器
    scheduler.start()

