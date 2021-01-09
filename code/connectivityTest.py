from threading import Thread
from queue import Queue
from fake_useragent import UserAgent
import requests
import json
from get_youneed import main as youneed
import base64

class CrawInfo(Thread):
    def __init__(self,ip):
        Thread.__init__(self)
        self.ip=ip

    def run(self):
        url = 'https://a.tool.lu/__tm.gif?'
        url1 = 'https://tool.lu/ip/ajax.html'
        headers1 = {
            'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_1_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36',
        }
        headers2 = {
            'referer': 'https://tool.lu/ip/',
            'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_1_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36',
        }
        params = {
            'domain': 'tool.lu',
            'url': 'https://tool.lu/ip/',
            'title': 'IP地址查询 - 在线工具',
            'referrer': 'https://www.google.com/',
            'sh': '1080',
            'sw': '1920',
            'cd': '24',
            'lang': 'zh-CN'
        }
        data = {'ip': self.ip}
        session = requests.session()
        resp = session.get(url=url, headers=headers1,params=params)
        try:
            resp1 = session.post(url=url1, headers=headers2, data=data)
            jsondata=json.loads(resp1.text)
            ipAttribution=jsondata['text']['ip2region']
            print(ipAttribution)
            # return ipAttribution
        except json.decoder.JSONDecodeError:
            print(ip,'无法获取归属地')

    # def getYouneed(self):
    #     res = youneed('v2ray')


if __name__ == "__main__":
    ipQueue=Queue()
    result = youneed('v2ray')
    for i in result:
        protocol = i[:8]
        content = i[8:]
        contentDecode = base64.b64decode(content).decode()
        contentJsonLoad = json.loads(contentDecode)
        ip = contentJsonLoad['add']
        ipQueue.put(ip)
    for i in range(0,3):
        craw=CrawInfo(ipQueue)
        craw.start()