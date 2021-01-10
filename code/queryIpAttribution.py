import requests
import json
import base64
from code.timeFormat import timeFormat


def checkip(ips):
    url = 'http://ip-api.com/batch?'
    params = {
        'fields': '24595',
        'lang': 'zh-CN'
    }
    headers = {
        'Content-Type': 'text/plain;charset=UTF-8',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_1_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36',
    }
    try:
        repo = requests.post(url=url, params=params, data=json.dumps(ips))
        return(repo.json())
    except requests.exceptions.ProxyError:
        print('端点限制为每分钟从IP地址发出15个请求，等1分钟后再尝试')

def queryIpAttribution(domain):
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
    data = {'ip': domain}
    session = requests.session()
    resp = session.get(url=url, headers=headers1, params=params)
    try:
        resp1 = session.post(url=url1, headers=headers2, data=data)
        jsondata = json.loads(resp1.text)
        ipAttribution = jsondata['text']['ip2region']
        return ipAttribution
    # print(ipAttribution)
    except json.decoder.JSONDecodeError:
        print(ip, '无法解析地址')

def testing(result):
    print(f'总共{len(result)}个v2服务器，下面进行IP归属地检测……')
    contentList = []
    for i in result:
        content = i[8:]
        contentDecode = base64.b64decode(content).decode()
        contentJsonLoad = json.loads(contentDecode)
        contentList.append(contentJsonLoad)
    iplist = []
    iparr = []
    for i in contentList:
        ip = i['add']
        # print(ip)
        iplist.append(ip)
        if len(iplist) == 100:
            iparr.append(iplist)
            iplist.clear()
    resultIP = []
    cont = 0
    for i in iparr:
        attribution = checkip(i)
        for j in range(len(attribution)):
            if attribution[j]['status'] == 'fail':
                # contentList[j+cont]['ps'] = contentList[j+cont]['add']
                continue
            else:
                contentList[j+cont]['ps'] = attribution[j]['countryCode'] + \
                    attribution[j]['country']+'_'+contentList[j+cont]['add']
            resultIP.append(contentList[j+cont])
        cont += 100

    protocol = 'vmess://'
    v2 = []
    for i in resultIP:
        s=str(i).replace('\'','\"')
        encode_v2=base64.b64encode(s.encode('utf-8')).decode('utf-8')
        v2.append(protocol+encode_v2)
    print(f'IP归属地查询成功，总计：{len(v2)}个')
    print('-'*42)
    return v2


# if __name__ == "__main__":
