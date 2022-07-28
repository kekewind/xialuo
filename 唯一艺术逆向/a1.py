# -*- coding: utf-8 -*-
# @Author  : 夏洛
# @File    : a1.py
# @VX : tl210329

import json
import random
import sys
import time
import urllib
import copyheaders
import execjs
import requests

execjs_str = """
    const CryptoJS  = require('crypto-js')

    var window = {}
    window.deciphering = function(e, t) {
            t = t || 32;
            for (var n = "ABCDEFGHJKMNPQRSTWXYZabcdefhijkmnprstwxyz2345678", o = n.length, i = 0; i < t; i++)
                n.charAt(Math.floor(Math.random() * o));
            console.log(e)
            return e
    }
    function  encryptSelf(t, a) {
                var s = CryptoJS.enc.Base64.parse('4tBlCLWFZ3eD93CvDE2lpw==')
                  , r = JSON.stringify({
                    id: t.substr(0, t.length - 1),
                    sum: a
                })
                  , i = CryptoJS.enc.Utf8.parse(r)
                  , _ = CryptoJS.AES.encrypt(i, s, {
                    mode: CryptoJS.mode.ECB,
                    padding: CryptoJS.pad.Pkcs7
                });
                return _.toString()
    }
    function aesDecrypt(encrypted) {
                var key = '5opkytHOggKj5utjZOgszg=='
                var t = CryptoJS.enc.Base64.parse(key)
                console.log(t.toString())
                var decrypted = CryptoJS.AES.decrypt(encrypted, t, {
                    mode: CryptoJS.mode.ECB,
                    padding: CryptoJS.pad.Pkcs7
                });
                decrypted = CryptoJS.enc.Utf8.stringify(decrypted).toString();
                var dataResultFun = decrypted.split(",")[0].substr(4)
                var dataResultId = decrypted.split(",")[1].split("=")[1]
                var sigresult = eval(dataResultFun)
                var sig = encryptSelf(dataResultId,sigresult)

                return {sigresult,sig,dataResultFun,dataResultId}
    }
    """

headers = copyheaders.headers_raw_to_dict(b"""
    accept: application/json, text/plain, */*
    accept-language: zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6
    cache-control: no-cache
    content-length: 338
    content-type: application/json;charset=UTF-8
    origin: https://theone.art
    pragma: no-cache
    referer: https://theone.art/
    sec-ch-ua: " Not A;Brand";v="99", "Chromium";v="98", "Microsoft Edge";v="98"
    sec-ch-ua-mobile: ?0
    sec-ch-ua-platform: "Windows"
    sec-fetch-dest: empty
    sec-fetch-mode: cors
    sec-fetch-site: same-site
    user-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36 Edg/98.0.1108.56
""")


def get_sig():
    dec_res = requests.get('https://api.xxx.art/market/api/key/get').json().get("data")
    cpl = execjs.compile(execjs_str)
    api_key = cpl.call("aesDecrypt", dec_res)
    print(f"解密前：{dec_res}")
    print(f"解密后：{api_key}")
    return api_key

def spider():
    api_key = get_sig()

    headers['sig'] = urllib.parse.quote(api_key.get("sig"))

    data_api = 'https://api.xxx.art/goods/api/saleRecord/list'
    page_ = 0

    while True:

        page_ += 1
        data = '{"authorId":null,"chainContract":null,"commodityCategoryId":null,' \
               '"commodityId":null,"highPrice":"","lowPrice":"","pageCount":' + str(page_) + ',' \
                                                                                             '"pageSize":20,"seriesWorks":null,"seriesWorksId":null,"sort":null,' \
                                                                                             '"statusSell":1,"topicId":null,"typeMarket":null,"sig":"' + api_key.get(
            "sig") + '"}'

        res = requests.post(data_api, headers=headers, json=json.loads(data)).json()

        if 'records' not in str(res):
            print(f'无法获取数据：{res}')
            sys.exit()

        time.sleep(random.uniform(0, 1.5))
        shop_list = res.get("data").get("records")

        for isp in shop_list:
            print(isp)

        if len(shop_list) < 20:
            print(f"暂无下一页：【exit】")


if __name__ == '__main__':
    get_sig()

