import re
import json
import requests
from requests.adapters import HTTPAdapter
from code.timeFormat import timeFormat
import base64


def getDataAddress(url):   # https://www.youneed.win
    session = requests.session()
    session.mount('https://', HTTPAdapter(max_retries=3))
    header = {
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36'}
    resp = session.get(url=url, headers=header)
    data = re.findall('ps_ajax = ({.*?})', resp.text)[0]
    js = json.loads(data)
    geturl = js['ajax_url']
    nonce = js['nonce']
    post_id = js['post_id']
    # url = 'https://www.youneed.win/wp-admin/admin-ajax.php'
    header = {'origin': 'https://www.youneed.win',
              'referer': 'https://www.youneed.win/free-ss',
              'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36'}
    data = {'action': 'validate_input',
            'nonce': nonce,
            'captcha': 'success',
            'post_id': post_id,
            'type': 'captcha'
            }
    resp = session.post(url=geturl, headers=header, data=data, timeout=10)
    j = json.loads(resp.text)
    table = j['content']
    return table


def get_v2ray(data):
    result = re.findall('data-raw="(.*?)"', data)

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
    return v2
    # return result


def checkip(ip):
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
        repo = requests.post(url=url, params=params, data=json.dumps(ip))
        return(repo.json())
    except requests.exceptions.ProxyError:
        print('端点限制为每分钟从IP地址发出15个请求，等1分钟后再尝试')


def get_SsOrSsr(data):
    result = re.findall('<td align="center">(.*?)</td>', data)
    return result


def ss_Data_sorting(ss):
    ss_list = []
    for i in range(0, len(ss), 4):
        server = ss[i]
        port = ss[i+1]
        method = ss[i+3]
        password = ss[i+2]
        sort = method+':'+password+'@'+server+':'+port
        base64_ss = base64.b64encode(sort.encode())
        ss_list.append('ss://'+base64_ss.decode("utf-8") +
                       '#'+server)
    return ss_list


def ssr_Data_sorting(ssr):
    ssr_list = []
    for i in range(0, len(ssr), 6):
        server = ssr[i]
        port = ssr[i+1]
        protocol = ssr[i+4]
        method = ssr[i+3]
        obfs = ssr[i+5]
        password = base64.b64encode(ssr[i+2].encode()).decode('utf-8')
        params_base64 = 'remarks=' + \
            base64.b64encode(server.encode()).decode('utf-8')

        sort = server+':'+port+':'+protocol+':'+method + \
            ':'+obfs+':'+password+'/?'+params_base64
        base64_ss = base64.b64encode(sort.encode())
        ssr_list.append('ssr://'+base64_ss.decode("utf-8"))
    return ssr_list


def main(param):
    v2ray_url = 'https://www.youneed.win/free-v2ray'
    ss_url = 'https://www.youneed.win/free-ss'
    ssr_url = 'https://www.youneed.win/free-ssr'

    if param == 'ss':
        output = ss_Data_sorting(get_SsOrSsr(getDataAddress(ss_url)))
    elif param == 'ssr':
        output = ssr_Data_sorting(get_SsOrSsr(getDataAddress(ssr_url)))
    elif param == 'v2ray':
        output = get_v2ray(getDataAddress(v2ray_url))
    elif param == 'ss*':
        output = ss_Data_sorting(get_SsOrSsr(getDataAddress(ss_url))) + \
            ssr_Data_sorting(get_SsOrSsr(getDataAddress(ssr_url)))
    elif param == 'all':
        output = get_v2ray(getDataAddress(v2ray_url)) + \
            ss_Data_sorting(get_SsOrSsr(getDataAddress(ss_url))) + \
            ssr_Data_sorting(get_SsOrSsr(getDataAddress(ssr_url)))
    elif param == 'v2ss':
        output = get_v2ray(getDataAddress(v2ray_url)) + \
            ss_Data_sorting(get_SsOrSsr(getDataAddress(ss_url)))
    else:
        output = []
    print(timeFormat(), '读取www.youneed.win_{}数据成功'.format(param))
    print('-'*42)
    return output


if __name__ == "__main__":
    # res = queryIpAttribution()
    res = main('ss')
    print(res)
    # queryIpAttribution()
