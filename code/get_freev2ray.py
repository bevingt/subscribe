import requests
from requests.adapters import HTTPAdapter
from code.timeFormat import timeFormat
import parsel

def freev2ray():  # https://view.freev2ray.org
    session = requests.session()
    session.mount('https://', HTTPAdapter(max_retries=3))
    url = 'https://view.freev2ray.org'
    header = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.1 Safari/605.1.15'}
    resp = session.get(url=url, headers=header, timeout=10)
    data = parsel.Selector(resp.text)
    result = data.xpath(
        '//*[@id="intro"]/div/div/footer/ul[1]/li[2]/button/@data-clipboard-text').extract()
    print(timeFormat(), '读取freev2ray数据成功')
    print('-'*42)
    return result

if __name__ == "__main__":
    resp=freev2ray()
    print(resp)