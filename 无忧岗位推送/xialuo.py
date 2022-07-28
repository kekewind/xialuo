# -*- coding: utf-8 -*-
# @Author  : 夏洛
# @File    : xialuo.py
# @VX : tl210329

import random
import re
import smtplib
import threading
import time
from email.mime.text import MIMEText

import redis
import requests
import pymysql as MySQLdb
from lxml import etree

proxy_api = 'http://http.tiqu.alibabaapi.com/getip?num=1&type=2&neek=563834&port=11&lb=1&pb=4&regions='
golols = {
    "dl": {
        'https': '16150'
    },
    "headers": {}
}


def get_hexxor(s1, _0x4e08d8):
    _0x5a5d3b = ''

    for i in range(len(s1)):
        if i % 2 != 0: continue
        _0x401af1 = int(s1[i: i + 2], 16)
        _0x105f59 = int(_0x4e08d8[i: i + 2], 16)
        _0x189e2c_10 = (_0x401af1 ^ _0x105f59)
        _0x189e2c = hex(_0x189e2c_10)[2:]
        if len(_0x189e2c) == 1:
            _0x189e2c = '0' + _0x189e2c
        _0x5a5d3b += _0x189e2c
    return _0x5a5d3b


def get_unsbox(arg1):
    _0x4b082b = [0xf, 0x23, 0x1d, 0x18, 0x21, 0x10, 0x1, 0x26, 0xa, 0x9, 0x13, 0x1f, 0x28, 0x1b, 0x16, 0x17, 0x19,
                 0xd,
                 0x6, 0xb, 0x27, 0x12, 0x14, 0x8, 0xe, 0x15, 0x20, 0x1a, 0x2, 0x1e, 0x7, 0x4, 0x11, 0x5, 0x3, 0x1c,
                 0x22, 0x25, 0xc, 0x24]
    _0x4da0dc = []
    _0x12605e = ''
    for i in _0x4b082b:
        _0x4da0dc.append(arg1[i - 1])
    _0x12605e = "".join(_0x4da0dc)
    return _0x12605e


def setheaders():
    headers = {
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
        'Host': 'jobs.51job.com',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36',
    }
    while True:
        try:
            r = requests.get('https://jobs.51job.com/beijing-dxq/134663856.html', headers=headers
                             , proxies=golols["dl"], timeout=(3, 5), verify=False)
            arg1s = re.findall("arg1=\'(.*?)\'", r.text)
            if len(arg1s) == 0:
                print(f"无法获取setcookie {arg1s} 尝试切换代理！")
                setproxy()
                time.sleep(4)
                continue
            break
        except  Exception as e:
            print(f"网络异常：{e}")
            setproxy()
    s1 = get_unsbox(arg1s[0])
    _0x4e08d8 = "3000176000856006061501533003690027800375"
    _0x12605e = get_hexxor(s1, _0x4e08d8)
    print(f"更新_0x12605e： {_0x12605e}")
    headers = {
        # 'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest',
        "cookie": "acw_sc__v2=%s" % _0x12605e,
    }
    golols["headers"] = headers


def get_page_searchdata(url):
    print(f">>> 正在访问：{url}")
    golols["headers"]["Accept"] = 'application/json, text/javascript, */*; q=0.01'
    while True:
        try:
            ssr = requests.get(url, headers=golols["headers"],
                               proxies=golols["dl"], verify=False,
                               timeout=(3, 3)
                               )
            if 'setCookie("acw_sc__v2", x)' in ssr.text:
                print(f">>> cookie失效")
                setheaders()
                continue

            if '<title>æ»‘åŠ¨éªŒè¯é¡µé¢</title>' in ssr.text:
                print(f'>>> ip失效')
                setproxy()
                setheaders()
                continue

            return ssr.json()

        except  Exception as e:
            print(f"网络异常：{e}")
            setproxy()


def search_keyword():
    url = f'https://search.51job.com/list/000000,000000,0000,00,9,99,%25E5%25A4%2596%25E8%25B4%25B8,2,1.html?lang=c&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&ord_field=1&dibiaoid=0&line=&welfare='
    page_source_data = get_page_searchdata(url)
    return page_source_data


def get_newjobs():
    rinset = redis.Redis(host="127.0.0.1", port=6379, db=9)

    if not rinset.exists('ids'):

        ### 只搜索第一页数据
        orgdata = search_keyword()
        engine_jds = orgdata.get("engine_jds")
        for jd in engine_jds:
            rinset.sadd('ids', jd.get("jobid"))
            print(f">>> 初始化插入；{jd.get('jobid')}")
        return []

    else:
        origindata = search_keyword()
        ### 然后在过滤操作 获取最新的数据 ，然后获取详情页推送消息
        listdata = origindata.get("engine_jds")
        ft = []
        for jb in listdata:

            if rinset.sismember('ids', jb.get("jobid")):
                jobid = jb.get("jobid")
                job_name = jb.get("job_name")
                company_name = jb.get("company_name")
                issuedate = jb.get("issuedate")
                text = f">>> 未发送变化 旧岗位：{jobid} {job_name} {company_name} {issuedate}"
                print(text)
                continue
            ft.append(jb)
            rinset.sadd('ids', jb.get("jobid"))

        ### 更新数据
        return ft


def dowork():
    print(f'\n正在执行任务：{time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())}')
    try:

        jobs_list = get_newjobs()

        for newjb in jobs_list:
            jobid = newjb.get("jobid")
            job_name = newjb.get("job_name")
            company_name = newjb.get("company_name")
            issuedate = newjb.get("issuedate")
            timesamp = time.mktime(time.strptime(issuedate,'%Y-%m-%d %H:%M:%S'))

            if time.time() - timesamp > 60*60:
                print(f">>> 时间差较大 取消发送 {jobid} {job_name} {company_name} {issuedate}")
            else:
                ###p
                compurl = newjb.get("company_href")
                jobcomaddreass = getaddress(compurl).strip().replace('公司地址：','')

                print("*" * 50)
                print("\n\n")
                print(">>>> 正在获取详情页：：：")
                print(f">>> 正在推送 {jobcomaddreass}  {jobid} {job_name} {company_name} {issuedate}")
                aend_email(jobcomaddreass,jobid,job_name,company_name,issuedate)
                print("\n\n")
                print("*" * 50)


    except Exception as e:

        print(f">>> 执行异常：{e}")


def aend_email(jobcomaddreass,jobid,job_name,company_name,issuedate):

    content = """
    工作地址：%s
    工作链接：%s
    工作名称：%s
    公司名称：%s
    发布时间：%s
    """ % (jobcomaddreass,f'https://jobs.51job.com/shanghai/{jobid}.html?s=sou_sou_soulb&t=0_0',job_name,company_name,issuedate)

    msg_from = '961948438@qq.com'  # 发送方邮箱
    passwd = 'ijomqjqxetxabcjf'  # 填入发送方邮箱的授权码
    msg_to = '961948438@qq.com'  # 收件人邮箱

    subject = "日志提醒"  # 主题
    msg = MIMEText(content)
    msg['Subject'] = subject
    msg['From'] = msg_from
    msg['To'] = msg_to
    try:
        s = smtplib.SMTP_SSL("smtp.qq.com", 465)
        s.login(msg_from, passwd)
        result = s.sendmail(msg_from, msg_to, msg.as_string())
        print(f">>>> 推送结果： {result}")
    except Exception as e:
        print(f">>> 发送失败：{e}")



def getaddress(company_href):
    while True:
        try:
            r = requests.get(company_href, headers=golols["headers"], proxies=golols["dl"], timeout=(3,5))

            if 'setCookie("acw_sc__v2", x)' in r.text:
                print(f">>> cookie失效")
                setheaders()

            if '<title>æ»‘åŠ¨éªŒè¯é¡µé¢</title>' in r.text:
                print(f'>>> ip失效')
                setproxy()
                setheaders()
            break
        except  Exception as e:
            print(f"网络异常：{e}")
            setproxy()
            setheaders()
            time.sleep(2)
    etree_html = etree.HTML(r.content.decode('gbk',errors='ignore'))
    allps = ''.join(etree_html.xpath('.//p[@class="fp"]//text()'))
    return allps if '地址' in allps else '-'

def init():
    res = requests.get('http://httpbin.org/get').json()
    ip = res.get("origin")
    base_api = f'https://ty-http-d.hamir.net/index/white/add?neek=tyhttp447242&appkey=7a708324dfca56cbaee3dcb908ca5198&white=' + ip
    res = requests.get(base_api).json()
    print(f'添加白名单状态：{res}')


def setproxy():
    try:
        time.sleep(random.randint(1, 3))
        res = requests.get(proxy_api)
        ip = (res.json().get("data")[0].get("ip") + ":" + res.json().get("data")[0].get("port"))
        golols['dl']["https"] = "https://" + ip
        print("https://" + ip)
    except Exception as e:
        print(e, "设置代理错误！")
        time.sleep(random.randint(1, 3))
        setproxy()


if __name__ == "__main__":
    ####创建时间调度器，每隔60分钟执行一次
    init()
    setproxy()
    setheaders()
    while True:
        th = threading.Thread(target=dowork)
        th.start()
        time.sleep(60)



