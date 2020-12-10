import parsel
import requests
from requests.adapters import HTTPAdapter
import time
from decode_ss import run

def ishadow():  # https://my.ishadowx.biz
    url = 'https://my.ishadowx.biz'
    header = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.1 Safari/605.1.15'}
    resp = session.get(url=url, headers=header, timeout=10)
    data = parsel.Selector(resp.text)
    vmess = data.xpath(
        '//div[@class="hover-text"]/h4/span/@data-clipboard-text').extract()
    vmess_url = []
    for i in vmess:
        u = i[:-1]
        vmess_url.append(u)
    print(timeformat(), '读取ishadow数据成功')
    print('-'*42)
    return vmess_url


def freev2ray():  # https://view.freev2ray.org
    url = 'https://view.freev2ray.org'
    header = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.1 Safari/605.1.15'}
    resp = session.get(url=url, headers=header, timeout=10)
    data = parsel.Selector(resp.text)
    vmess = data.xpath(
        '//*[@id="intro"]/div/div/footer/ul[1]/li[2]/button/@data-clipboard-text').extract()
    print(timeformat(), '读取freev2ray数据成功')
    print('-'*42)
    return vmess


# def freess():  # https://io.freess.info/#portfolio-preview  救援网址:f55.fun 或 55r.run
#     from PIL import Image
#     from io import BytesIO
#     from pyzbar.pyzbar import decode
#     import base64
#     url = 'https://io.freess.info/'
#     header = {
#         'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.1 Safari/605.1.15'}
#     resp = session.get(url=url, headers=header, timeout=10)
#     data = parsel.Selector(resp.text)
#     jpg_list = data.xpath(
#         '//*[@id="portfolio-preview"]/div/div//@href').extract()
#     for jpg in jpg_list:
#         jpg_base64 = jpg.split(',')[1]  # 取图片加密数据
#         resp_img = base64.b64decode(jpg_base64)  # 解码
#         img = Image.open(BytesIO(resp_img))  # 读取解码后的图片数据
#         txt_list = decode(img)  # 二维码解码
#         ss = []
#         for txt in txt_list:
#             barcodeData = txt.data.decode("utf-8")
#             ss.append(barcodeData)
#             # print(barcodeData)
#     print(timeformat(), '读取freess数据成功')

#     return ss
def netlify():  # https://jiang.netlify.app/
    url='https://jiang.netlify.app/'
    header={
            'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36'}
    resp=requests.get(url=url,headers=header)
    return resp.text


def free_v2ray():   # https://www.youneed.win
    import json
    import re
    url='https://www.youneed.win/free-v2ray'
    header={
              'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36'}
    resp=session.get(url=url,headers=header)
    data=re.findall('ps_ajax = ({.*?})',resp.text)[0]
    js=json.loads(data)
    geturl=js['ajax_url']
    nonce=js['nonce']
    post_id=js['post_id']
    # url = 'https://www.youneed.win/wp-admin/admin-ajax.php'
    header = {'origin': 'https://www.youneed.win',
              'referer': 'https://www.youneed.win/free-v2ray',
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
    vmess = re.findall('data-raw="(.*?)"', table)

    print(timeformat(), '读取free_v2ray数据成功')
    print('-'*42)
    return vmess
    # print(vmess)


def main():
    heroku = ['vmess://eyJwb3J0IjoiNDQzIiwicHMiOiJ2MnJheS0xLWhvbWVtZWRpYSIsInRscyI6InRscyIsImlkIjoiYWQ4MDY0ODctMmQyNi00NjM2LTk4YjYtYWI4NWNjODUyMWY3IiwiYWlkIjoiNjQiLCJ2IjoiMiIsImhvc3QiOiJsaXR0bGUtdG9vdGgtMjExNy5iZXZpbmd0LndvcmtlcnMuZGV2IiwidHlwZSI6Im5vbmUiLCJwYXRoIjoiXC8iLCJuZXQiOiJ3cyIsImFkZCI6IjEwNC4yNC4xMzcuMTAzIn0=',
              'vmess://eyJwb3J0IjoiNDQzIiwicHMiOiJ2MnJheS0yLWhvbWVtZWRpYSIsInRscyI6InRscyIsImlkIjoiYWQ4MDY0ODctMmQyNi00NjM2LTk4YjYtYWI4NWNjODUyMWY3IiwiYWlkIjoiNjQiLCJ2IjoiMiIsImhvc3QiOiJjb2xkLWZsb3dlci1lZDhhLmJldmluZ3Qud29ya2Vycy5kZXYiLCJ0eXBlIjoibm9uZSIsInBhdGgiOiJcLyIsIm5ldCI6IndzIiwiYWRkIjoiMS4wLjAuMCJ9', 
              'vmess://eyJwb3J0IjoiNDQzIiwicHMiOiJ2MnJheS0zLWhvbWVtZWRpYSIsInRscyI6InRscyIsImlkIjoiYWQ4MDY0ODctMmQyNi00NjM2LTk4YjYtYWI4NWNjODUyMWY3IiwiYWlkIjoiNjQiLCJ2IjoiMiIsImhvc3QiOiJjcmltc29uLW1vdW50YWluLTZjODQuYmV2aW5ndC53b3JrZXJzLmRldiIsInR5cGUiOiJub25lIiwicGF0aCI6IlwvIiwibmV0Ijoid3MiLCJhZGQiOiIxMDQuMjQuMTM3LjEwMyJ9']
    vmess = heroku+ishadow()+freev2ray()+free_v2ray()+run()
    # vmess = ishadow()+freev2ray()+freess()
    print(timeformat(), '合并数据')
    print('-'*42)
    return vmess


def merge():
    s = ''
    v_url = main()
    for i in range(len(v_url)):
        if i == len(v_url)-1:
            s = s + v_url[i]
        else:
            s = s + v_url[i]+'\n'
    return s


def base64_encode():
    import base64
    data = merge()
    # netlify=netlify()
    subscribe = base64.b64encode(data.encode())
    with open('list.txt', 'w', encoding='utf-8') as f:
        f.write(subscribe.decode("utf-8")+'\n')
        f.write(netlify())
    print(timeformat(), '保存成功')
    
    # print(subscribe)


# def clash():  # URLEncode 处理后，生产clash订阅地址
#     vmess = merge()
#     url = 'https://www.urlencoder.org/'
#     header = {
#         'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.1 Safari/605.1.15'}
#     data = {'input': vmess, 'charset': 'UTF-8', 'separator': 'lf'}
#     resp = requests.post(url=url, headers=header, data=data, timeout=10)
#     select = parsel.Selector(resp.text)
#     encodeurl = select.xpath('//*[@id="output"]/text()').extract_first()
#     dingyue = 'https://homecloud.work:320/sub?target=clash&url={}&insert=false'.format(
#         encodeurl)
#     print(timeformat(), '完成订阅转换')
#     return dingyue


# def copy():
#     import pyperclip  # 粘贴板模块
#     pyperclip.copy(clash())
#     print('复制链接成功')
#     return


# def w_yaml():
#     import yaml
#     c = clash()
#     with open("/Users/allian/.config/clash/free.yaml", "r", encoding='utf-8') as f:
#         yaml_obj = yaml.load(f.read(), Loader=yaml.Loader)
#         yaml_obj["proxy-providers"]['Free']['url'] = c
#     with open("/Users/allian/.config/clash/free.yaml", "w", encoding='utf-8') as f:
#         yaml.dump(yaml_obj, f, default_flow_style=False)
#     print(timeformat(), '保存成功！')


def timeformat():
    return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())


if __name__ == "__main__":
    session = requests.session()
    session.mount('https://', HTTPAdapter(max_retries=3))
    base64_encode()

