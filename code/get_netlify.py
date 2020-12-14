import requests
import base64
from requests.adapters import HTTPAdapter
from code.timeFormat import timeFormat


def netlify():  # https://jiang.netlify.app/
    session = requests.session()
    session.mount('https://', HTTPAdapter(max_retries=3))
    url = 'https://jiang.netlify.app/'
    header = {
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36'}
    resp = session.get(url=url, headers=header)
    result = base64.b64decode(resp.text).decode()
    arr_list = result.split('\n')[:-1]
    return arr_list


def distinguishTheAgreement(data):
    ss = []
    v2ray = []
    trojan = []
    ssr = []
    for i in data:
        if i.find('ss://') == 0:
            ss.append(i)
        elif i.find('ssr://') == 0:
            ssr.append(i)
        elif i.find('vmess://') == 0:
            v2ray.append(i)
        elif i.find('trojan://') == 0:
            trojan.append(i)
        else:
            continue
    return ss, ssr, v2ray, trojan


def main(param):
    resp = netlify()
    ss, ssr, v2ray, trojan = distinguishTheAgreement(resp)
    if param == 'ss':
        output = ss
    elif param == 'ssr':
        output = ssr
    elif param == 'v2ray':
        output = v2ray
    elif param == 'ss*':
        output = ss + ssr
    elif param == 'all':
        output = v2ray + ss + ssr + trojan
    elif param == 'v2ss':
        output = v2ray + ss
    elif param == 'vstro':
        output = v2ray+ss+trojan
    elif param == 'sstro':
        output = ss+trojan
    else:
        output = []
    print(timeFormat(), '读取jiang.netlify.app_{}数据成功'.format(param))
    print('-'*42)
    return output


if __name__ == "__main__":
    res = main('trojan')
    print(res)
